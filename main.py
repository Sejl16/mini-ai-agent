from agent import run_agent, extract_info
from tools import (
    calculator,
    add_task,
    list_tasks,
    web_search,
    read_file
)

print("AI Agent Started")
print("Type exit or bye to quit")

while True:

    user_message = input("\nYou: ").strip()

    if user_message.lower() in ["exit", "bye"]:
        print("Agent closing...")
        break

    # Extract JSON
    if user_message.startswith("/extract"):

        text = user_message.replace("/extract", "").strip()

        result = extract_info(text)

        print("\nJSON Output:")
        print(result)

        continue

    # Calculator
    if user_message.lower().startswith("calculator "):

        expression = user_message[len("calculator "):]

        print(calculator(expression))

        continue

    # Add Task
    if user_message.lower().startswith("add task "):

        task = user_message[len("add task "):]

        print(add_task(task))

        continue

    # List Tasks
    if user_message.lower() in ["list tasks", "Show task"]:

        print(list_tasks())

        continue

    # Search
    if user_message.lower().startswith("search "):

        query = user_message[len("search "):]

        print(web_search(query))

        continue

    # Read File
    if user_message.lower().startswith("read file "):

        file_path = user_message[len("read file "):]

        print(read_file(file_path))

        continue

    # Normal Agent
    answer = run_agent(user_message)

    print(f"\nAgent: {answer}")