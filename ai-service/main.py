from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_service import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_ai(request: AskRequest):
    try:
        answer = ask_llm(request.question)
        return {
            "question": request.question,
            "answer": answer
        }
    except Exception as e:
        return {
            "question": request.question,
            "answer": f"Error: {str(e)}"
        }








