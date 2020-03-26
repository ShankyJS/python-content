# A closure is a function that generates a new function, and can access through the namespace to all the variables.

def show_message(message):
    message = message.title() # local
    def show():
        print(message)
    return show

new_function = show_message("Shankyjs")
new_function()