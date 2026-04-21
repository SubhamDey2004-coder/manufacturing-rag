import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "tinyllama"

def generate_answer(query, context):
    prompt = f"""
Answer the question using ONLY the given context.

Do NOT add any new information.
Do NOT repeat the context.
Rewrite the answer clearly and simply.

Question: {query}

Context:
{context}

Provide:
- Clear steps (numbered)
- Keep it short and understandable
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
        }
    )
    data = response.json()
    
    print(response.json())
    
    # Safe Parsing
    if "response" in data:
        return data["response"]
    
    elif "message" in data:
        return data["message"]["content"]
    else:
        return str(data)