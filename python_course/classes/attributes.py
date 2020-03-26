class Circle:
    pi = 3.14159265

    def __init__(self, radio):
        self.radio = radio  # Instance variable

circle_a = Circle(10)
circle_b = Circle(20)

circle_b.radio = 100


print(circle_a.radio) #our instance can use the instance variable

print(circle_b.radio)

print (Circle.pi) # We can use without do any instance