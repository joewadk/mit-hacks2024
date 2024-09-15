import base64
import requests
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
import pg
import sms
load_dotenv()
from flask_cors import CORS

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)
# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

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
