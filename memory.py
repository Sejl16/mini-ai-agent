from collections import deque

memory = deque(maxlen=10)

def  add_memory(role, content):
    memory.append({
        "role": role,
        "content":content
    })

def get_memory():

    return list(memory)

# add_memory("user", "Hello")
# add_memory("assistant", "Hi")

# print(get_memory())