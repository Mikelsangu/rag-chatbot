 IMPORTANTE:"El troceado simple por caracteres funciona pero genera ruido, una mejora futura sería trocear respetando límites de frase o párrafo"
 # RAG Chatbot

Chatbot de inteligencia artificial que responde preguntas sobre documentos propios usando la técnica RAG (Retrieval-Augmented Generation). El modelo de lenguaje consulta únicamente el contenido de los documentos cargados, sin inventar información externa.

## Stack tecnológico

- **Python 3.11** + **FastAPI** — API REST del backend
- **ChromaDB** — Base de datos vectorial para búsqueda semántica
- **Ollama** + **Llama 3.1 8B** — Modelo de lenguaje corriendo en local (GPU)
- **LangChain** — Orquestación del pipeline RAG
- **Flutter** — Interfaz de usuario (repositorio separado)

## Requisitos previos

- Python 3.11
- [Ollama](https://ollama.com) instalado con el modelo `llama3.1:8b`
- GPU recomendada para rendimiento óptimo

## Instalación

1. Clona el repositorio
2. Crea el entorno virtual e instala dependencias:

```bash
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
```

3. Carga tus documentos en ChromaDB:

```bash
python cargar_pdf.py
```

4. Arranca el servidor:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`. Documentación interactiva en `http://127.0.0.1:8000/docs`.

## Uso

Envía una petición POST al endpoint `/preguntar`:

```json
{
  "pregunta": "¿Qué es un ataque de phishing?"
}
```

## Interfaz visual

La interfaz Flutter está disponible en [rag-chatbot-app](https://github.com/Mikelsangu/rag-chatbot-app).

## Autor

Mikel Sangüesa — Estudiante DAM + Título en IA (UNIR)