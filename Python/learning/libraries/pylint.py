# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------
# [1] Pylint Is A Code Analysis Tool
# [2] It Checks Your Code For Errors
# [3] It Checks Your Code Style
# [4] It Checks Your Code Complexity
# [5] It Checks Your Code For Best Practices
# [6] It Checks Your Code For Security Issues
# [7] It Checks Your Code For Performance Issues
# [8] It Checks Your Code For Documentation Issues
# [9] It Checks Your Code For Compatibility Issues
# [10] It Checks Your Code For Code Smells
# [11] It Checks Your Code For Code Quality
# [12] It Checks Your Code For Code Readability
# [13] To install pylint on Linux use the command: sudo apt-get install pylint
# [14] To install pylint on Windows use the command: pip install pylint
# [15] To check the code by pylint write pylint libraries/pylint.py

"""
This is My Module
To Create Function
To Say Hello
"""

def say_hello(name: str) -> str:
    """
    This Function Says Hello To Someone.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    msg = "Hello"
    return f"{msg} {name}"


if __name__ == "__main__":
    print(say_hello("Ahmed"))
#new line

