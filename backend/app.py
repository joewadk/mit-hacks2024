from flask import Flask, request, jsonify
import base64
import requests
import os
<<<<<<< HEAD
from flask import Flask, request, jsonify
import pg
import sms
=======
from dotenv import load_dotenv
import pg  
import sms  
>>>>>>> 72ac711787a4f571756c2a033d6705367b753fa2
load_dotenv()
from flask_cors import CORS

app = Flask(__name__)

OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')

<<<<<<< HEAD
app = Flask(__name__)
CORS(app)
# Function to encode the image
=======
>>>>>>> 72ac711787a4f571756c2a033d6705367b753fa2
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

<<<<<<< HEAD
# Scan route
@app.route('/scan', methods=['POST'])
def scan_images():
    try:
        # Get images from the POST request (assumes images are sent as file uploads)
        image_files = request.files.getlist('images')

        if len(image_files) != 3:
            return jsonify({"error": "Exactly 3 images are required"}), 400

        image_lists = []

        # Encode images
        for image_file in image_files:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            image_lists.append(image_base64)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What’s in this image?"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_lists[0]}"}},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_lists[1]}"}},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_lists[2]}"}}
                    ]
                }
            ],
            "max_tokens": 300
        }

        # Send request to OpenAI API
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()

        # Extract and return the content of the response
        llm_response = response_data['choices'][0]['message']['content']
        return jsonify({"response": llm_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to query data from the database and send it to the frontend
@app.route('/pills', methods=['POST'])
def get_data():
    try:
        # Query the data from the 'jawad' table using pg.py's query_data function
        rows = pg.query_data('jawad')
        
        # Check if data exists
        if not rows:
            return jsonify({"error": "No data found"}), 404
        
        # Process the rows into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "prescription_name": row[0],
                "raw_instruction": row[1],
                "expiration_date": row[2],
                "expected_time1": row[3],
                "expected_time2": row[4],
                "expected_time3": row[5]
            })

        # Return the data as a JSON response
        return jsonify({"data": data}), 200

    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True,port=5000)
=======
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
>>>>>>> 72ac711787a4f571756c2a033d6705367b753fa2
