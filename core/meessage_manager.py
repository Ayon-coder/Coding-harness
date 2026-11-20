
import json
from pathlib import Path


class Messages:

    def __init__(self):
        self.messages = []

        self.project_root = Path(__file__).resolve().parent.parent
        self.history_dir = self.project_root / "history"
        self.history_dir.mkdir(exist_ok=True)

        self.txt_file = self.history_dir / "conversation.txt"
        self.json_file = self.history_dir / "conversation.json"

        self.load_history()

    def append(self, message):

        self.messages.append(message)

        # Save readable log
        with open(self.txt_file, "a", encoding="utf-8") as file:
            role = message.get("role", "unknown")
            file.write(f"\n[{role.upper()}]\n")
            file.write(f"{message.get('content', '')}\n")
            file.write("-" * 50 + "\n")

        self.save_history()

    def save_history(self):

        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4, ensure_ascii=False)

    def load_history(self):

        if self.json_file.exists():
            try:
                with open(self.json_file, "r", encoding="utf-8") as file:
                    self.messages = json.load(file)

                print("[History loaded successfully]")

            except (json.JSONDecodeError, OSError) as error:
                print(f"[History loading error]: {error}")
                self.messages = []

    def get_messages(self):
        return self.messages
