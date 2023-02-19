FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Return all todos from the given filepath."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)