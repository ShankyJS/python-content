class Animal:
    def eat(self):
        print("I'm eating!")

    def sleep(self):
        print("I'm sleeping")

    def common(self):
        print("This is a common method")


class Pet:
    def adoption_dates(self, date):
        self.adoption_date = date

    def common(self):
        print("This is a pet method")


class Dog(Animal, Pet):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("I'm barking mthafkc***")

    def common(self):
        print("This is a dog method")

    def sleep(self):
        print(self.name, "is sleeping") #override method
        Animal.sleep(self)
        print("Don't bored me")


class Cat(Animal, Pet):
    def __init__(self, name):
        self.name = name

    def mew(self):
        print("Meowwwwww")


nonis = Dog("Nonis")
mishi = Cat("Mishi")

# nonis.adoption_dates("Now")
# print(nonis.adoption_date)

nonis.sleep()

# This looks from the children, if the method is not there, will look into his parents.
# nonis.common()
