import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"


def generate_answer(query, context):
    prompt = f"""
Answer the question using ONLY the given context.

Do NOT add new information that is not supported by the context.
Do NOT repeat the context verbatim.
Rewrite the answer clearly and simply.

Question:
{query}

Context:
{context}

Provide:
- Clear troubleshooting steps
- Numbered steps where appropriate
- A short, understandable response
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1
            }
        },
        timeout=120,
    )
    response.raise_for_status()

    data = response.json()

    if "response" in data:
        return data["response"]

    if "message" in data and "content" in data["message"]:
        return data["message"]["content"]

    raise RuntimeError("Ollama returned an unexpected response format.")
