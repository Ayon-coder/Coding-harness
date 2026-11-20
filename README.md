# Coding Harness

Coding Harness is a terminal-based AI coding assistant powered by a local Ollama model. It provides a styled CLI, conversation history, and tool-calling support.

## Requirements

- Windows 10/11, macOS, or Linux
- Python 3.14 or newer
- [Ollama](https://ollama.com/) installed and running

## Quick Start

### 1. Clone the repository

```powershell
git clone https://github.com/Ayon-coder/Coding-harness.git
cd Coding-harness
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

Using `pip`:

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

Using `uv`:

```powershell
uv sync
```

### 4. Install and start Ollama

Install Ollama, then download a model:

```powershell
ollama pull qwen3-coder
```

Start the Ollama service if it is not already running:

```powershell
ollama serve
```

### 5. Configure the environment

Create a `.env` file in the project root:

```dotenv
OLLAMA_HOST=http://localhost:11434
MODEL_NAME=qwen3-coder
```

Replace `qwen3-coder` with any Ollama model you have installed.

> Keep `.env` private. It is included in `.gitignore` and should not be committed.

### 6. Run the CLI

From the project root:

```powershell
python main.py
```

You can also use the console script:

```powershell
harness
```

## Using the Harness

Enter a coding request at the `You:` prompt. The harness will stream the model response and can execute configured tools when requested.

Commands:

- `exit` - close the application
- `quit` - close the application
- `Ctrl+C` - close the application

## Conversation History

Messages are stored in:

- `history/conversation.json`
- `history/conversation.txt`

The JSON file is loaded automatically when the harness starts.

## Project Structure

```text
coding-harness/
├── config/              # Environment and system settings
├── core/
│   ├── harness.py       # Main agent loop
│   ├── llm.py           # Ollama streaming integration
│   └── meessage_manager.py
├── history/             # Saved conversation history
├── tools/               # Tool definitions and implementations
├── ui/
│   └── cli.py           # Rich terminal interface
├── main.py              # Application entry point
└── pyproject.toml       # Package and dependency configuration
```
