'''
    A demo program that shows how to define and run a
    variety of functions.
    
    In Python you cannot overload functions (same name with different
    numbers of arguments).  
'''


def print_welcome():
    """
    A function that doesn't accept any arguments.
    """
    print("Welcome to the Future Value Calculator")
    print()


def print_message(message):
    """
    Function that accepts one argument.  We dynamically enter the message
    now.
    """
    print(message)
    print()


#Call the functions.
print_welcome()
print_message("Test Message")
