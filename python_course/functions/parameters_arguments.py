def create_user(name="John", last_name="Doe", age=18):
    return {
        'name': name,
        'last_name': last_name,
        'complete_name': "{} {}".format(name, last_name),
        'age': age
    }


Shanky = create_user("Jhan", "Silva", 19)

print(Shanky["name"])
print(Shanky["last_name"])
print(Shanky["age"])
