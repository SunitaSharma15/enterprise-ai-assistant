import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

def get_embedding(text: str):
    return model.encode(text).tolist()

def load_documents():
    file_path = "data/company_policy.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = [line.strip() for line in content.split("\n") if line.strip()]

    existing = collection.count()
    if existing > 0:
        return

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[get_embedding(chunk)]
        )

def search_documents(query: str):
    results = collection.query(
        query_embeddings=[get_embedding(query)],
        n_results=3
    )

    return results["documents"][0]