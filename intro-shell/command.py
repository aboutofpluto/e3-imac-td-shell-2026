"""
Simple command to get help or run built-in functions
"""

def check(command):
    """
    checks if a command can be called
    parameters:
    - command: string, a python built-in function (hopefully)
    return value:
    True is 'command' is a callable function, otherwise False
    """
    try:
        eval(command)
    except Exception as e:
        print("Invalid command {}: {}".format(command, e))
        return False
    if callable(eval(command)) is False:
        print("Invalid command {}: not callable".format(command))
        return False
    return True


def run(command, params=""):
    """
    runs a command with optional parameters
    prints the result of the command
    parameters:
    - command: string, a python built-in function
    - params: a string containing a comma-separated list of parameters
    return value: None
    """
    if check(command):
        print(eval(command)(*params.split(",")))

        
if __name__ == "__main__":
    command = input("Command? ")
    action = input("Action (run|help)? ")

    if action == "run":
        params = input("Optional parameters (comma-separated)? ")
        run(command, params)
    else:
        help(command)
