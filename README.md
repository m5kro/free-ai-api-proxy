# free-ai-api-proxy
A simple proxy to send API requests to free llm sites with the right headers. Goal is to be a fake openAI API. Unicode is supported.<br>
# Goals
1. Add other openai API options ✅<br>
2. Also send old messages ✅<br>
3. Return in openai json format ✅<br>
# How to use
```pip install -r requirements.txt``` <br>
```python3 llama2-api.py``` <br>
or <br>
```python3 blackbox-api.py```<br>
<br>
The API will start on http://127.0.0.1:5000/api <br>
Model Options For llama2:<br>
meta/llama-2-70b-chat<br>
meta/llama-2-13b-chat<br>
meta/llama-2-7b-chat<br>
yorickvp/llava-13b<br>
nateraw/salmonn<br>
<br>
Model Options For blackbox:<br>
blackbox-code<br>
blackbox-chat<br>
<br>
Other Options:<br>
max_tokens (1-4096)<br>
temperature (llama2 only)<br>
top_p (llama2 only)<br>
<br>
You can try the api with:<br>
```python3 test-api.py``` <br>
The prompts and commands were copied off of the openai docs. (link and model was changed to use proxy)

