course = "Python"
version = "3"

# Replace values with variables

# result = "Course of %s %s" % (course, version)

# Using the format module
result = "Course of {a} {b}".format(a = course, b = version)

print(result)