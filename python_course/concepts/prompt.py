# Input every returns a String.

name = input("What is your name?\n")
age = int(input("What is your age?\n"))
weight = float(input("What is your actual weight (KG)?\n"))
authorized = input("Are you authorized? (yes/no)\n") == "yes"


print("Hello", name, "Your age is:", age, "and your weight is", weight)
print("Authorized?:", authorized)
