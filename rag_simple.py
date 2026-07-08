import chromadb
import ollama

# Conectamos con la base de datos vectorial que ya tienes
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="tema_seguridad_informatica")

def preguntar(pregunta):
    # Paso 1: recuperar contexto relevante de ChromaDB
    resultados = collection.query(
        query_texts=[pregunta],
        n_results=4
    )
    documentos_relevantes = resultados['documents'][0]
    contexto = "\n".join(documentos_relevantes)

    # Paso 2: construir el prompt incluyendo ese contexto
    prompt = f"""Usa el siguiente contexto para responder la pregunta. Si el contexto no contiene información relevante, dilo claramente.

Contexto:
{contexto}

Pregunta: {pregunta}

Respuesta:"""

    # Paso 3: mandar todo a Llama
    respuesta = ollama.chat(
        model='llama3.1:8b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    print("Contexto recuperado:")
    print(contexto)
    print("\nRespuesta del modelo:")
    print(respuesta['message']['content'])

# Prueba
preguntar("¿Qué es el Esquema Nacional de Seguridad?")