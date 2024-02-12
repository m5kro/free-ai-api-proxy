# llama-ai-api-proxy
A simple proxy to send API requests to https://www.llama2.ai/api with the right headers. Goal is to be a fake openAI API<br>
# How to use
```pip install -r requirements.txt``` <br>
```python3 llama2-api.py``` <br>
The API will start on http://127.0.0.1:5000/api <br>
You can try the api with ```curl http://127.0.0.1:5000/api   -H "Content-Type: application/json"   -H "Authorization: Bearer $OPENAI_API_KEY"   -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
        "role": "user",
        "content": "Compose a poem that explains the concept of recursion in programming."
      }
    ]
  }'```

