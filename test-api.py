from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:5000/api", api_key="bearer nokey")

completion = client.chat.completions.create(model="blackbox-code",
messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Knock knock."},
  {"role": "assistant", "content": "Whos there?"},
  {"role": "user", "content": "Orange."}
])

print(completion.choices[0].message.content)
