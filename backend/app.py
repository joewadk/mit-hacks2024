from flask import Flask, request, jsonify
import base64
import requests
import os
from dotenv import load_dotenv
import pg  
import sms  
load_dotenv()

app = Flask(__name__)

OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@app.route('/get_chat', methods=['GET'])
def get_chat():
    user_query = request.args.get('query', default='', type=str)  
    image_lists = []

    for i in range(1, 4):
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
                        "text": user_query  #insert query from frontend here!
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
    llm_response = response.json()['choices'][0]['message']['content']
    return jsonify({"response": llm_response})


@app.route('/chat', methods=['POST'])
def post_chat():
    data = request.json
    prescription_name = data.get('prescription_name')
    raw_instruction = data.get('raw_instruction')
    expiration_date = data.get('expiration_date')
    expected_time1 = data.get('expected_time1')
    expected_time2 = data.get('expected_time2')
    expected_time3 = data.get('expected_time3')

    # Call the insert_data function from pg.py
    pg.insert_data(
        prescription_name,
        raw_instruction,
        expiration_date,
        expected_time1,
        expected_time2,
        expected_time3
    )
    return jsonify({"message": "Data inserted successfully"}), 201

# Route to send SMS using the sms.py script
@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    recipient_email = data.get('recipient_email')
    sms_body = data.get('sms_body')

    # Call the send_sms function from sms.py
    result = sms.send_sms(recipient_email, sms_body)
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)
