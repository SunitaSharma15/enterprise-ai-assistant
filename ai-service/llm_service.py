import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful enterprise AI assistant. Give clear and concise answers."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content