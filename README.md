# code-llama
This is a simple demonstration of code-llama using ollam toolkits + Gradio.

1. Code-Llama: https://ai.meta.com/blog/code-llama-large-language-model-coding/
2. Ollama: https://github.com/ollama/ollama
3. Gradio: https://www.gradio.app/

## Implementations

### Install  the ollama.
1. `curl -fsSL https://ollama.com/install.sh | sh `
2. Pull the Model `ollama run codellama` (7B Parameter, 3.8GB Model Size)
3. Create own Model with Prompt. We can create a modelfile like below:
   ```
   FROM codellama

    ## Set the Temperature
    PARAMETER temperature 1
    
    ## set the system prompt
    SYSTEM """
    You are a expert software developer designed multiple software system in AWS and Python.
    Please answer all the python code related questions being asked and keep it very professionally and politely. 
    """
    ```
4. Run to create model: `ollama create mymodel -f ./Modelfile`
5. test with CLI: `ollama run mymodel` and ask all type of questions
6. Start the Ollama server: `ollama serve` and can be configured with env variable like:
   ```
   sudo OLLAMA_MODELS=/usr/share/ollama/.ollama/models OLLAMA_HOST=127.0.0.1:8080 ollama serve
   ```
   For other variables: `ollama serve --help`
7. Make a POST request: 
    ```
    curl http://0.0.0.0:8080/api/generate -d '{
         "model": "example",
         "prompt":"Why is the sky blue?"
       }'
    ```

## Serve with UI:
1. Install `pip install gradio`.
2. We can use gradio text fields:

```
   interface = gr.Interface(
       fn=make_a_post_request_function,
       inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
       outputs="text"
   )
```
2. **make_a_post_request_function()** will make a /POST request to Ollama server with Payload.


## Images:
