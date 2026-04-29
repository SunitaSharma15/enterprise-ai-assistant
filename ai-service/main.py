from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag_service import load_documents, search_documents
from llm_service import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_documents()

class AskRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_ai(request: AskRequest):
    try:
        docs = search_documents(request.question)
        answer = ask_llm(docs, request.question)

        return {
            "question": request.question,
            "context": docs,
            "answer": answer
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}"
        }