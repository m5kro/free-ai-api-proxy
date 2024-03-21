import requests
import json
import random
import string

# Define the boundary string
boundary = '----WebKitFormBoundary2MMRhsDtRApSbuEB'

# Define the data to be sent
data = {
    '1': '{"id":"6dabd75144784c470301df503cf710e1e58d7989","bound":null}',
    '2': '{"id":"8473c166548e62f0bab6d11c822840a17a442a4d","bound":null}',
    '0': '[{"action":"$F1","options":{"onSetAIState":"$F2"}},{"chatId":"j7IlaaV","messages":[]},"You are now a helpful AI assistant. Now respond to the following question: hi"]'
}

# Define the headers
headers = {
    'Host': 'demo.rowenaai.com',
    'Cookie': '__Host-authjs.csrf-token=5b6c39397f626fd6625ffcfa536ccf5a756f5cd4b36abb51b19268d2a958f351%7C6ad2edb9ffa28bf5e921f211e1db30b56db4aed1b0923c80472beeea16070c11; __Secure-authjs.callback-url=https%3A%2F%2Fdemo.rowenaai.com',
    'Content-Length': '523',
    'Content-Type': 'multipart/form-data; boundary=' + boundary,
    'Accept': 'text/x-component',
    'Next-Action': '6ed51a8d1a1a0222478e92cb5c3357db14052913',
    'Origin': 'https://demo.rowenaai.com'
}

def isolate_line_starting_with_2(multiline_string):
    lines = multiline_string.split('\n')  # Split the multiline string into lines
    for line in lines:
        if line.strip().startswith('2:'):
            return line.strip()  # Return the line starting with '2:'
    return None

def generate_random_string(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Construct the request body
body = ''
for key, value in data.items():
    body += '--{}\r\n'.format(boundary)
    body += 'Content-Disposition: form-data; name="{}"\r\n\r\n'.format(key)
    body += value + '\r\n'

body += '--{}--\r\n'.format(boundary)

# Send the request
response = requests.post('https://demo.rowenaai.com/', headers=headers, data=body)

# Extract the part of the response that starts with "2:"
response_text = response.text
relevant_part = isolate_line_starting_with_2(response_text)

# Remove "2:" from the string
relevant_part = relevant_part.replace("2:", "")

# Parse the remaining part as JSON
try:
    response_json = json.loads(relevant_part)
    messages = response_json['messages']
    for message_id, message_data in sorted(messages.items())[:-1]:
        print(f"Message ID: {message_id}")
        for message in message_data:
            print(f"Role: {message.get('role')}")
            print(f"Content: {message.get('content')}")
            print("-------------------")
except ValueError:
    print("Failed to parse JSON response.")


