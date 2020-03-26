def tabla_multiplicar(number, max=10):
    for position in range(1, max+1):
        yield number * position, number, position #returns the value of the iteration without stop the bucle.

for result, number, position in tabla_multiplicar(9, 20):
    print(number,"*",position,"=", result)
