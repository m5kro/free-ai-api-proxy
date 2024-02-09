# llama-ai-api-proxy
A simple proxy to send API requests to https://www.llama2.ai/api with the right headers. <br>
# How to use
```pip install -r requirements.txt``` <br>
```python3 llama2-api.py``` <br>
The API will start on http://127.0.0.1:5000/api <br>
You can try the api with ```curl -X POST -H "Content-Type: application/json" -d '{"prompt": "when was nato founded."}' http://localhost:5000/api```

