from functools import wraps


# Closures
def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

hi_func()
bye_func()


# Function Decorators
def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executing here before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


# Decorator functions allow us to add functionality to the original function by adding this to the wrapper function
# without modifying the original function
# @decorator_function allows you to add the decorator function's functionality on top of the original function
# whenever the original function is called i.e. the same as the code below:
# display = decorator_function(display)
# Note that the usual syntax is @func_name where func_name is the name of the decorator function
# We need to have the wrapper function having the same number of arguments as the original function so that they can be
# passed through

# Class decorators

class decoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    # Same behaviour as the wrapper function
    def __call__(self, *args, **kwargs):
        print(f"call method executing here before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decoratorClass
def display():
    print("Display function ran!")


@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")


display()
display_info("Shrimat", 20)

# Examples of using decorators: Logging when a function is executed in a separate log file
# or timing the execution for a function
# Problem: adding multiple decorators to the same function acts as a nested function call by definition
# hence the incorrect function name is passed to the decorator due to the return statement
# using the wraps tool from functools wraps the inner function name with the wrapper
