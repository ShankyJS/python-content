dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, "h": 8}

del dictionary["a"]
value = dictionary.pop("b")

# dictionary = {}
dictionary.clear()

print(value)
print(len(dictionary))
print(dictionary)