
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """  Read a text file and return a list
     of t-do-items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        # print(todos_local)
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Open the saved file and writes additional
    to-do items in the file
     """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# print(__name__)
if __name__ == '__main__':
    print(get_todos())
    print(help(get_todos))
    # print(write_todos())
    print(__name__)
