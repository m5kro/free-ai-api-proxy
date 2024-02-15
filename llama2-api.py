from flask import Flask, request, jsonify
import requests
import json
import re

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

# Credit to Dan McDougall (liftoff) for trailing comma cleaner
def remove_trailing_commas(json_like):
    trailing_object_commas_re = re.compile(
        r'(,)\s*}(?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    trailing_array_commas_re = re.compile(
        r'(,)\s*\](?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    # Fix objects {} first
    objects_fixed = trailing_object_commas_re.sub("}", json_like)
    # Now fix arrays/lists [] and return the result
    return trailing_array_commas_re.sub("]", objects_fixed)

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def process_prompt():
    # Get the received data and clean it
    received_data = json.loads(remove_trailing_commas(request.get_data(as_text=True)))
    
    # Find the system prompt
    sysP = received_data['messages'][0]['content']
    
    # Find the first question
    P = received_data['messages'][1]['content']
    
    # Add to the prompt
    prompt = "<s>[INST] <<SYS>>\\n" + sysP + "\\n<</SYS>>\\n\\n" + P + " [/INST]\\n"
    
    # Add any other messages to the prompt and format correctly
    for i, message in enumerate(received_data['messages']):
        if i >= 2:
            content = message['content']
            if message['role'] == "assistant":
                prompt += content + "</s>"
            elif message['role'] == "user":
                prompt += "<s>[INST] " + content + " [/INST]\\n"
            else:
                # If assistant or user is not the role
                return jsonify({'error': 'Message Role missing or misspelled for messages after system prompt. Must be either "assistant" or "user"'})
    print(f"Final Prompt: {prompt}")

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
