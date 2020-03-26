#snake_case parameter
def create_message(name):
    return "Hello {}, welcome to the Python 3 course".format(name)


new_message = create_message("Shanky")
print(new_message)

# ------------------------------------------------------------------------


def addition(val1, val2, val3):
    return val1 + val2 + val3


result = addition(10, 30, 20)
print(result)

# ------------------------------------------------------------------------


def get_course():
    return "Course of Python", "Basic", 3.6


course, level, version = get_course()

print(course, level, version)
