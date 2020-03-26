# Dado de los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.
print("Welcome to the area calculator in python.")
base = float(input("What is the base of your triangle?\n"))
height = float(input("What is the height of your triangle?\n"))
area = base * height
print("The area of your triangle with base:",
      base, "and height: ", height, " is: ", area)
