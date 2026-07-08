import chromadb

# Creamos un cliente de ChromaDB que guarda los datos en disco, en una carpeta local
client = chromadb.PersistentClient(path="./chroma_db")

# Una "collection" es el equivalente a una tabla en SQL
collection = client.get_or_create_collection(name="documentos_prueba")

# Insertamos varios textos de ejemplo
collection.add(
    documents=[
        "El gato duerme en el sofá durante toda la tarde.",
        "Los perros son animales muy leales a sus dueños.",
        "Python es un lenguaje de programación muy usado en inteligencia artificial.",
        "Java es ampliamente usado en aplicaciones empresariales y backend.",
        "Madrid es la capital de España y tiene mucho tráfico.",
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

print("Documentos insertados correctamente.")
print("Total de documentos en la colección:", collection.count())