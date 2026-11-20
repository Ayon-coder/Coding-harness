import ollama
from config.config import settings

class LLM:

    def __init__(self):

        self.model = settings.MODEL_NAME

    def generate(self, messages, tools = None):

        response = ollama.chat(
            model = self.model,
            messages=messages,
            tools=tools,
            stream=False
        )

        return response

    def stream(self, messages, tools = None):

        response = ollama.chat(
            model = self.model,
            messages=messages,
            tools=tools,
            stream=True
        )

        return response

