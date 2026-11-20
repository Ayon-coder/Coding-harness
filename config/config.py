import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

class Settings:

    OLLAMA_HOST = os.getenv("OLLAMA_HOST")
    MODEL_NAME = os.getenv("MODEL_NAME")

    TEMPERATURE = 0.7
    TOP_P = 0.9
    NUM_CTX = 4096

    # Agent Configuration
    MAX_ITERATIONS = 5

    SYSTEM_PROMPT = """
    You are an intelligent AI coding assistant.

    Your responsibilities:
    - Understand user requests.
    - Write clean and maintainable code.
    - Debug existing code.
    - Explain programming concepts.
    - Analyze project structures.
    - Help implement software features.

    Rules:
    1. Understand the user's intention before answering.
    2. Ask questions if essential information is missing.
    3. Never assume files or dependencies exist.
    4. Provide complete code when requested.
    5. Explain errors and their solutions.
    6. Be concise and technically accurate.
    7. Never claim to have executed code unless you actually did.

    Always prioritize correctness and usefulness.
    """

    # Conversation Configuration
    MAX_HISTORY = 20


settings = Settings()