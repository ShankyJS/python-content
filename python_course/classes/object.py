class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Duck(object):
    def __init__(self, name):  # Init is not the constructor of the class.
        self.name = name

    def __str__(self):
        return self.name


cat = Cat("Bigotes")
cat.age = "6"
duck = Duck("Lucas")

print(cat.__dict__)
print(duck.__dict__)
