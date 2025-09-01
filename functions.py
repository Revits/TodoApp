FILEPATH = "todos.txt"
#custom function for avoiding repetitive codes
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_write, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
         file_local.writelines(todo_write)
