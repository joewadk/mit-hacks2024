import base64
import requests
from dotenv import load_dotenv
import os
import pg
import sms

load_dotenv()

OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

image_lists = []

for i in range(1,4):
    base64_image = encode_image(f"./images/img{i}.webp")
    image_lists.append(base64_image)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {OPEN_AI_KEY}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image? "#filler for prompt to be received from frontend
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_lists[0]}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_lists[1]}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_lists[2]}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json()['choices'][0]['message']['content'])