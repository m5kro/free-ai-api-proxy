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
    "temperature": 0.6,
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
    prompt = "<s>[INST] <<SYS>>\n" + received_data.get('systemPrompt', '') + "\n<</SYS>>\n\n" + received_data.get('prompt', '') + " [/INST]\n"
    
    if prompt:
        # Modify the 'data' with the received prompt
        data['prompt'] = prompt
        data['systemPrompt'] = received_data.get('systemPrompt', '')
        # Make the request to the llama2.ai API
        response = requests.post(url, headers=headers, json=data)

        # Return the response from llama2.ai
        return response.text
    else:
        return jsonify({'error': 'No prompt provided'})

if __name__ == '__main__':
    app.run(port=5000)
