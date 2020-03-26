class Circle:
    pi = 3.141592654
    
    @classmethod
    def area(cls, radius):
        return cls.pi * radius**2

result = Circle.area(10)

print(result)