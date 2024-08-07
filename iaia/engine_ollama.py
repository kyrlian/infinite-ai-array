import requests
import os

# Ollama exposes port 11434 by default

class Ollama_Engine:
    def __init__(self, model_id="llama3", port=11434):
        self.model = model_id
        self.url = f"http://localhost:{port}/api"
        self.headers = {"Content-Type": "application/json"}
        self.verbose = bool(os.environ.get("IAIA_VERBOSE"))

    def list(self):
        response = requests.get(f"{self.url}/tags", headers=self.headers)
        if response.status_code == 200:
            response_json = response.json()
            models = response_json["models"]
            modelnames = [m["name"] for m in models]
            return modelnames
        else:
            print("Error:", response.status_code, response.text)

    def generate_response(self, prompt, model=None, temperature=None, max_tokens=None, stop=[]):
        if model is None:
            model = self.model
        options={"temperature":temperature, "num_predict":max_tokens, "stop":stop}
        data = {"model": model, "stream": False, "prompt": prompt, "options":options}
        response = requests.post(f"{self.url}/generate", headers=self.headers, json=data)
        response_json = response.json()
        if self.verbose:
            print("Response JSON:", response_json)
        return response_json

    def generate_text(self, prompt, model=None, temperature=None, max_tokens=None, stop=[]):
        response_json = self.generate_response(prompt, model, temperature, max_tokens, stop)
        actual_response = response_json["response"]
        return actual_response

llm_engine = Ollama_Engine()
