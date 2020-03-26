# Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla.

# Converter functions


def celsiusToFahrenheit(grades_quantity):
    total = (grades_quantity * 9/5) + 32
    print("Your", grades_quantity, "celsius are equal to:", total, "fahrenheit")


def fahrenheitToCelsius(grades_quantity):
    total = (grades_quantity - 32) * 5/9
    print("Your", grades_quantity, "fahrenheit are equal to:", total, "celsius")


# Entering the menu
print("Welcome to the temperature converter made on Python")
option = int(input(
    "Press 1 to convert Celsius to Fahrentein, press 2 to convert Fahrenheit to Celsius\n"))

if option == 1:
    grades = float(
        input("Please insert how many Celsius grades you want to convert\n"))
    celsiusToFahrenheit(grades)

elif option == 2:
    grades = float(
        input("Please insert how many Fahrenheit grades you want to convert\n"))
    fahrenheitToCelsius(grades)
