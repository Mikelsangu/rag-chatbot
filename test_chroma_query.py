import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="documentos_prueba")

# Pregunta que NO coincide textualmente con ninguna frase guardada
resultados = collection.query(
    query_texts=["¿Qué lenguajes se usan para programar software?"],
    n_results=2
)

for doc, distancia in zip(resultados['documents'][0], resultados['distances'][0]):
    print(f"Distancia: {distancia:.4f} -> {doc}")