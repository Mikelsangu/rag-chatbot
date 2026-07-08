from pypdf import PdfReader
import chromadb

# Paso 1: extraer todo el texto del PDF
reader = PdfReader("10612639_full_7911187_Tema_10._Seguridad_informatica_esl-ES.pdf")
texto_completo = ""
for pagina in reader.pages:
    texto_completo += pagina.extract_text() + "\n"

print(f"Total de caracteres extraídos: {len(texto_completo)}")

# Paso 2: trocear el texto en fragmentos con solapamiento
def trocear_texto(texto, tamano_chunk=700, solapamiento=100):
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano_chunk
        chunks.append(texto[inicio:fin])
        inicio += tamano_chunk - solapamiento
    return chunks

fragmentos = trocear_texto(texto_completo)
print(f"Número de fragmentos generados: {len(fragmentos)}")

# Paso 3: meter los fragmentos en una nueva collection de ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="tema_seguridad_informatica")

ids = [f"fragmento_{i}" for i in range(len(fragmentos))]
collection.add(documents=fragmentos, ids=ids)

print("Documento cargado correctamente en ChromaDB.")
print("Total de fragmentos en la collection:", collection.count())