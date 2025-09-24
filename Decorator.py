#    A decorator is just a function that modifies another function 
#    without changing its actual code


#QUESTION POWER FUNCTION
import math

# Decorator function
def my_decorator(func):
    def wrapper(x):
        print(f"Calling function {func.__name__} with argument {x}")
        result = func(x)   # call the actual function
        print(f"Result: {result}")
        return result
    return wrapper   

# Apply decorator
@my_decorator
def square(x):
    return math.pow(x, 2)


# Example usage
square(5)


