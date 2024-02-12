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
    sysP = received_data['messages'][-2]['content']
    P = received_data['messages'][-1]['content']
    
    prompt = "<s>[INST] <<SYS>>\n" + sysP + "\n<</SYS>>\n\n" + P + " [/INST]\n"
    
    if P and P != "":
        # Set the model
        data['model'] = received_data['model']
        # Modify the 'data' with the received prompt
        data['prompt'] = prompt
        data['systemPrompt'] = sysP
        # Set Max Tokens if given
        if "max_tokens" in received_data:
            data['maxTokens'] = received_data['max_tokens']
        # Set temperature if given
        if "temperature" in received_data:
            data['temperature'] = received_data['temperature']
        # Set top p if given
        if "top_p" in received_data:
            data['topP'] = received_data['top_p']
        # Make the request to the llama2.ai API
        response = requests.post(url, headers=headers, json=data)

        # Return the response from llama2.ai
        return response.text
    else:
        return jsonify({'error': 'No prompt provided'})

if __name__ == '__main__':
    app.run(port=5000)
