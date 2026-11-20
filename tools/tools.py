
import json
from pathlib import Path


# Load tool definitions
TOOLS_FILE = Path(__file__).with_name("tools.json")

with open(TOOLS_FILE, "r", encoding="utf-8") as file:
    tools = json.load(file)


# Tool implementations

def list_files(path="."):
    return [item.name for item in Path(path).iterdir()]


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return f"Successfully wrote {path}"


# Tool registry
available_functions = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file
}
