import os
import time
import random
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_log():
    logs = [
        "Processing request...",
        "Executing task...",
        "Preparing data...",
        "Performing operation..."
    ]
    return random.choice(logs)

def write_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

@app.route('/')
def process_api():
    time.sleep(3)  # Wait for 3 seconds
    log_message = generate_log()
    print(f"Log: {log_message}")  

    # Update the log path
    log_directory = '/logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    random_text = f"log_{time.time()}.txt"
    file_path = os.path.join(log_directory, random_text)
    
    write_to_file(file_path, log_message)  # Write the log message to a file
    
    return f"Log: {log_message}"

@app.route('/download_external_logs', methods=['GET'])
def download_external_logs():
    env = request.args.get('env')
    
    # Fetch integration keys from environment variables
    integration_keys = {
        'development': os.getenv('DEV_INTEGRATION_KEY'),
        'staging': os.getenv('STAGING_INTEGRATION_KEY'),
        'production': os.getenv('PROD_INTEGRATION_KEY')
    }
    
    if env not in integration_keys:
        return jsonify({"error": "Invalid environment"}), 400

    external_api_url = "https://api.example.com/download_logs"
    headers = {
        "Authorization": f"Bearer {integration_keys[env]}"
    }

    try:
        response = requests.get(external_api_url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
