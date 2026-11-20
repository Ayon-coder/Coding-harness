import json
from config.config import settings
from .llm import LLM
from .meessage_manager import Messages
from tools.tools import tools, available_functions

class Harness:

    def __init__(self):
        self.llm = LLM()
        self.max_iter = 10
        self.messages = Messages()
        self.messages.append({
            "role": "system",
            "content": settings.SYSTEM_PROMPT
        })

    def run(self, user_input):

        self.messages.append({
            "role": "user",
            "content": user_input
        })

        for _ in range(self.max_iter):

            response = self.llm.stream(
                self.messages.get_messages(),
                tools = tools
            )
            ass_content = ""
            tool_calls = []

            for chunk in response:

                message = chunk.message

                if message.content:
                    ass_content += message.content
                    print(message.content, end="", flush=True)

                if message.tool_calls:
                    tool_calls.extend(message.tool_calls)

            print()

            ass_msg = {
                    "role": "assistant",
                    "content": ass_content
                }

            if tool_calls:
                ass_msg["tool_calls"] = [
                    call.model_dump(exclude_none = True)
                    for call in tool_calls
                ]
            self.messages.append(ass_msg)

            if not tool_calls:

                return ass_content

            for tool_call in tool_calls:
                func_name = tool_call.function.name
                arguments = tool_call.function.arguments
                print(f"\n[Executing Tool: {func_name}]")

                function = available_functions.get(func_name)

                if function is None:
                    result = f"Error: Unknown tool {func_name}"
                else:
                    try:
                        result = function(**arguments)

                    except Exception as error:
                        result = f"Tool execution error: {str(error)}"

                if not isinstance(result, str):
                    result = json.dumps(result, default=str)

                print(f"[Tool Result]: {result}")

                # Send tool result back to LLM
                self.messages.append({
                    "role": "tool",
                    "name": func_name,
                    "content": result
                })

        print("\nMaximum iterations reached.")
        return None
