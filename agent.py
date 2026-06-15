from openai import OpenAI
import os
from dotenv import load_dotenv
import json

from tools import (
    calculator,
    add_task,
    list_tasks,
    web_search,
    read_file
)

from memory import add_memory
from memory import get_memory

load_dotenv(dotenv_path=".env")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

TOOLS_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a math expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read contents of a text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string"
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "Add a task to the task list",
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "Task to add"
                    }
                },
                "required": ["task"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_tasks",
            "description": "Show all tasks",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


def extract_info(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Extract information from text. Return ONLY valid JSON."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content


def run_agent(user_message):
    messages = [
        {
            "role": "system",
            "content": """
            You are a helpful AI Assistant.
            Rules:
            - Give short and clean answers.
            - Do NOT use markdown tables.
            - Use tools whenever required.
            """
        }
    ]

    messages.extend(get_memory())
    messages.append({"role": "user", "content": user_message})

    while True:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=TOOLS_SCHEMAS
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            add_memory("user", user_message)
            add_memory("assistant", msg.content)
            return msg.content

        messages.append(msg)

        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            print(f"\nTool Requested: {name}")
            result = TOOLS[name](**args)
            print(f"Tool Result: {result}")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })


TOOLS = {
    "calculator": calculator,
    "add_task": add_task,
    "list_tasks": list_tasks,
    "web_search": web_search,
    "read_file": read_file
}

print("Agent file loaded")