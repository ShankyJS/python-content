# Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.

COP_CURRENCY = 0.00025
DOLLAR_CURRENCY = 4176.51

print("Welcome to the rate converter made on Python. You have two options:")
option = int(input(
    "To convert from USD to COP press 1, if you want to convert COP to USD press 2.\n"))

if option == 1:
    quantity = float(input("Insert your USD quantity: "))
    total = quantity * DOLLAR_CURRENCY
    print(total)

elif option == 2:
        quantity = float(input("Insert your COP quantity: "))
        total = quantity * COP_CURRENCY
        print(total)
