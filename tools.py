from pathlib import Path
from duckduckgo_search import DDGS

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid expression"
    
tasks = []

def read_file(file_path):

    try:
        return Path(file_path).read_text()

    except Exception as e:
        return str(e)

def add_task(task):
    try:
        tasks.append(task)
        return f"task added {task}"
    
    except Exception as e:
        return str(e)

def list_tasks():
    try:
        if not tasks:
            return "No task"
        return "\n".join(tasks)
    except Exception as e:
        return str(e)

def clear_tasks():
    try:
        tasks.clear()
        return "All tasks cleared."
    except Exception as e:
        return str(e)

def web_search(query):
    try:
        with DDGS() as ddgs:
            results = list(
                ddgs.text(query, max_results=5)
            )
        return str(results)
    except Exception as e:
        return str(e)




TOOLS = {
    "calculator": calculator,
    "add_task": add_task,
    "list_tasks": list_tasks,
    "web_search": web_search,
    "read_file": read_file
}

