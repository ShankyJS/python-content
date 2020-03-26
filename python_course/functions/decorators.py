# A decorator can modify a minimun of 3 functions.
# a, b ,c
#a(b) -> c


def decorator(function):
    def new_function(*args, **kwargs):
        print("Before the function")
        result = function(*args, **kwargs)
        print("We can add code after the function.")
        return result
    return new_function


@decorator
def function_a_decorate():
    print("This is a function to decorate")


function_a_decorate()

print("\n")
@decorator
def sum(val1, val2):
    return val1 + val2


result = sum(10, 20)

print(result)
