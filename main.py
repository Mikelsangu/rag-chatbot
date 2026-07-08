from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import chromadb
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="tema_seguridad_informatica")

# Esto define la forma del JSON que esperamos recibir en el body de la petición
class Pregunta(BaseModel):
    pregunta: str

@app.post("/preguntar")
def preguntar(datos: Pregunta):
    resultados = collection.query(
        query_texts=[datos.pregunta],
        n_results=4
    )
    documentos_relevantes = resultados['documents'][0]
    contexto = "\n".join(documentos_relevantes)

    prompt = f"""Usa el siguiente contexto para responder la pregunta. Si el contexto no contiene información relevante, dilo claramente.

Contexto:
{contexto}

Pregunta: {datos.pregunta}

Respuesta:"""

    respuesta = ollama.chat(
        model='llama3.1:8b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return {
        "pregunta": datos.pregunta,
        "respuesta": respuesta['message']['content']
    }