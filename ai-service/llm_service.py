import requests

def ask_llm(context_docs, question):
    context = "\n".join(context_docs)

    system_prompt = """
You are an enterprise knowledge assistant.
Answer only from the provided context.
If the answer is not found, say:
'Information not found in documents.'
Keep the answer concise and professional.
"""

    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "stream": False
        }
    )

    data = response.json()
    return data["message"]["content"]