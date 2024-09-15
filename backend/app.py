from flask import Flask, request, jsonify
import base64
import requests
import os
from dotenv import load_dotenv
import pg  
import sms  
load_dotenv()
from flask_cors import CORS
from difflib import SequenceMatcher

OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

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


@app.route('/chat-bot', methods=['POST'])
def chat_bot():
    data = request.json
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_KEY}"
    }
    medical_data=pg.query_data('jawad')
    context = ""
    for idx, row in enumerate(medical_data):
        context += f"\nPrescription {idx + 1}:\n"
    for i, item in enumerate(row):
        context += f"Field {i + 1}: {item}\n"
    if 'question' not in data or 'context' not in data:
        return jsonify({"error": "Both 'question' and 'context' fields are required"}), 400

    prompt = f"""
    You are the ai realtime assistant for PillPal. 
    Answer the following question: {data['question']}
    
    Here is the context to the conversation: {data['context'],context}
    Please format as human-readable as possible. Do not simply paste the medical data for the user to read. You must construct human-readable responses.
    Your role is to be an assistant. If they have questions about what medications theyre taking, when to take it, and how to take it, you will always have the answer.
    do not tell me what prescriptions they are taking. just answer their questions. do not spit out information from context out of context.
    """

    payload = {
        "model": "gpt-4o",  # Use the correct model name
        "messages": [
            {
                "role": "user",
                "content": prompt  # Pass the prompt as a single string
            }
        ],
        "max_tokens": 300
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        # Handle unsuccessful responses
        if response.status_code != 200:
            return jsonify({"error": f"OpenAI API request failed with status {response.status_code}"}), response.status_code

        # Extract the LLM's response
        llm_response = response.json()['choices'][0]['message']['content']
        return jsonify({"answer": llm_response}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
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

@app.route('/input_data', methods=['POST'])
def input_data():
    try:
        # Get JSON data from the frontend POST request
        data = request.json

         # Extract the individual values from the received JSON and log them
        prescription_name = data['prescription_name']
        raw_instruction = data['raw_instruction']
        expiration_date = data['expiration_date'] if data['expiration_date'] else None
        expected_time1 = data.get('expected_time1') if data['expected_time1'] else None
        expected_time2 = data.get('expected_time2') if data['expected_time2'] else None
        expected_time3 = data.get('expected_time3') if data['expected_time3'] else None


        # Call the insert_data function from pg.py to insert or update the data
        pg.insert_data(prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3)
        print(expiration_date)
        print("Inserting data:", prescription_name, raw_instruction, expiration_date, expected_time1, expected_time2, expected_time3)
        # Return a success message
        return jsonify({"message": "Record inserted/updated successfully"}), 200

    except KeyError as e:
        # Handle missing fields in the request
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        # Handle any other errors
        return jsonify({"error": str(e)}), 500
# Directory where uploaded images will be saved
UPLOAD_FOLDER = './images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload_images', methods=['POST'])
def upload_images():
    try:
        if 'images' not in request.files:
            return jsonify({"error": "No files provided"}), 400

        files = request.files.getlist('images')

        for file in files:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

        return jsonify({"message": "Images uploaded successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True, port=5000)
