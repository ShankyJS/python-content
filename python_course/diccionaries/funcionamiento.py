# # Declare the dictionary
# dictionary = {}

# # Add a key with his value
# dictionary["name"] = "Codi"

# # Get a value from a Key
# value = dictionary["name"]

# dictionary["name"] = 90
# print(dictionary)
# print(value)


# 4 override the last value of 1
dictionary = {"a": 1, "b": 2, "c": 3, "a": 4}

# Returns a boolean
# result = "a" in dictionary


# WIth get we don't get the key error and we can pass a text for errors. HIGLY RCOMMEND
result = dictionary.get("z", "No se encuentra la llave")

# This code will create the new key and value if doesn't exist, returns a new empty dictionary.
result = dictionary.setdefault("z", {})


# If we put a key that doesn't exist between the keys we will get the error KeyError
result = dictionary["z"]

print(result)
print(dictionary)
