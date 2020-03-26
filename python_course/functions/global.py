animal = "Lion" # Global scope variable

def show_animal():
    animal = "Monkey" #This value just exists on the function namespace or context.
    print(animal)

show_animal()
print(animal)