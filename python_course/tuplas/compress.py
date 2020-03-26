tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla_two = (100, 200, 300, 400)
# Generate new tuplas with zip

result = zip(tupla, lista, tupla_two)
result = tuple(result)

print(result)


# # one, two, three, four = tupla[0], tupla[1], tupla[2], tupla[3]
# # one, two, three, *four = tupla
# one, *two, five, six = tupla

# print(one)
# print(two)
# print(five)
# print(six)
