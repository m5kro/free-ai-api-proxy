from flask import Flask, request, jsonify
import requests

url = "https://www.llama2.ai/api"
headers = {
    "Content-Type": "application/json",
    "Referer": "https://www.llama2.ai/"
}
data = {
    "prompt": "When was nato founded?",
    "model": "meta/llama-2-70b-chat",
    "systemPrompt": "You are a helpful assistant.",
    "temperature": 0.7,
    "topP": 0.1,
    "topK": 40,
    "maxTokens": 1800,
    "image": None,
    "audio": None
}

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process_prompt():
    received_data = request.get_json()
    prompt = "You are a coder that follows orders exactly. <s>[INST] " + received_data.get('prompt', '') + " [/INST]"
    
    if prompt:
        # Modify the 'data' with the received prompt
        data['prompt'] = prompt

        # Make the request to the llama2.ai API
        response = requests.post(url, headers=headers, json=data)

        # Return the response from llama2.ai
        return response.text
    else:
        return jsonify({'error': 'No prompt provided'})

if __name__ == '__main__':
    app.run(port=5000)
