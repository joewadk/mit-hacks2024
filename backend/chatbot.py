import os
import requests
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("model_id")
baseten_api_key = os.getenv("baseten_api_key")

BASE_URL = f"https://model-{MODEL_ID}.api.baseten.co/production/predict"


def call_llamas3(question):
    headers = {
        "Authorization": f"Api-Key {baseten_api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are a knowledgeable healthcare assistant specializing in answering questions about medications. You provide accurate, easy-to-understand information about dosage, side effects, interactions, and usage instructions. You do not give medical advice or make diagnoses, and you encourage users to consult healthcare professionals for personalized advice.",
            },
            {"role": "user", "content": question},
        ],
        "stream": True,
        "max_tokens": 2800,
        "temperature": 0.5,
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload, stream=True)

        if response.status_code == 200:
            for content in response.iter_content():
                print(content.decode("utf-8"), end="", flush=True)
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Error calling the Llama model API: {e}")
        return None


if __name__ == "__main__":
    user_question = input("Please enter your medication question: ")
    call_llamas3(user_question)
