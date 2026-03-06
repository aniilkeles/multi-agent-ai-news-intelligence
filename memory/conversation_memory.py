memory = []

def add_message(role, content):

    memory.append({
        "role": role,
        "content": content
    })

def get_memory():

    return memory[-6:]