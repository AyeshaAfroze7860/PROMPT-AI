
import requests

def generate_response(prompt):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.2:3b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful prompt engineering assistant. "
                    "Provide clear and accurate answers."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        url,
        json=payload,
        timeout=180
    )

    response.raise_for_status()

    result = response.json()
    return result["message"]["content"]
