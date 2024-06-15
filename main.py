import json

import gradio as gr
import requests
from requests import HTTPError

url = "http://0.0.0.0:8080/api/generate"

headers = {

    'Content-Type': 'application/json'
}

history = []


def make_a_post_request_to_ollama_serve(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "example",
        "prompt": final_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response = response.text
            data = json.loads(response)
            actual_response = data['response']
            return actual_response
        else:
            raise HTTPError(f'Error: \n {response.text}')
    except HTTPError as h:
        print(h)


interface = gr.Interface(
    fn=make_a_post_request_to_ollama_serve,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Python Query"),
    outputs="text"
)
interface.launch()
