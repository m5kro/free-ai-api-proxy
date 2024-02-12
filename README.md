# llama-ai-api-proxy
A simple proxy to send API requests to https://www.llama2.ai/api with the right headers. Goal is to be a fake openAI API<br>
# Goals
1. Add other openai API options<br>
2. Also send old messages<br>
# How to use
```pip install -r requirements.txt``` <br>
```python3 llama2-api.py``` <br>
The API will start on http://127.0.0.1:5000/api <br>
Model Options:<br>
meta/llama-2-70b-chat<br>
meta/llama-2-13b-chat<br>
meta/llama-2-7b-chat<br>
yorickvp/llava-13b<br>
nateraw/salmonn<br>
<br>
Other Options:<br>
max_tokens (1-4096)<br>
temperature<br>
top_p<br>
<br>
You can try the api with ```curl http://127.0.0.1:5000/api   -H "Content-Type: application/json"   -H "Authorization: Bearer $NO-KEY-NEEDED"   -d '{
    "model": "meta/llama-2-70b-chat",
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

