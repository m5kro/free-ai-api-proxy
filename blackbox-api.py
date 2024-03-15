from flask import Flask, request, jsonify
import requests
import json
import re
import time

url = "https://www.blackbox.ai/api/chat"
headers = {
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Referer": "https://www.blackbox.ai/",
	"Content-Type": "application/json",
	"Origin": "https://www.blackbox.ai",
	"Alt-Used": "www.blackbox.ai"
}

data = {
	"messages": [],
	"id": "",
	"previewToken": None,
	"userId": "",
	"codeModelMode": True,
	"agentMode": {},
	"trendingAgentMode": {},
	"isMicMode": False,
	"userSystemPrompt":"Explain this code",
	"maxTokens":1024,
	"webSearchMode":False,
	"promptUrls":"",
	"isChromeExt":False,
	"githubToken":None
}

response = {
	"id": "chat-free",
	"choices": [
		{
			"finish_reason": "stop",
			"index": 0,
			"logprobs": None,
			"message": {
				"content": "Orange who?",
				"role": "assistant",
				"function_call": None,
				"tool_calls": None
			}
		}
	],
	"created": 1704461729,
	"model": "real-human-brain",
	"object": "chat.completion",
	"system_fingerprint": None,
	"usage": {
		"completion_tokens": 0,
		"prompt_tokens": 0,
		"total_tokens": 0
	}
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

@app.route('/api/chat/completions', methods=['POST'])
def process_prompt():
	# Set the timestamp for response
	response['created'] = int(round(time.time()))

	# Get the received data and clean it
	received_data = json.loads(remove_trailing_commas(request.get_data(as_text=True)))

	# Find the system prompt
	data["userSystemPrompt"] = received_data['messages'][0]['content']

	# Add any other messages to the prompt and format correctly
	for i, message in enumerate(received_data['messages']):
		if i >= 1:
			if message['role'] == "assistant":
				data['messages'].append({"id":"","content": message['content'],"role": "assistant"})
			elif message['role'] == "user":
				data['messages'].append({"id":"", "content": message['content'],"role": "user"})
			else:
				# If assistant or user is not the role
				return jsonify({'error': 'Message Role missing or misspelled for messages after system prompt. Must be either "assistant" or "user"'})

	if "model" not in received_data:
		return jsonify({'error': 'No model provided'})
	elif received_data['model'] == "blackbox-code":
		data["codeModelMode"] = True
	elif received_data['model'] == "blackbox-chat":
		data["codeModelMode"] = False
	else:
		return jsonify({'error': 'Invalid model provided'})
	# Set the model
	response['model'] = received_data['model']
	# Set Max Tokens if given
	if "max_tokens" in received_data:
		data['maxTokens'] = received_data['max_tokens']
	print("Data before sending:", data)
	# Make the request to the blackbox.ai API
	blackbox_response = requests.post(url, headers=headers, json=data)
	# Add the response to the json
	response['choices'][0]['message']['content'] = blackbox_response.text
	# Return the formatted json
	return response

if __name__ == '__main__':
	app.run(port=5000)
