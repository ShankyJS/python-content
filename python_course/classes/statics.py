class Triangle:
    number = 2 
    @staticmethod
    def area(base, height):
        return (base * height) / Triangle.number

result = Triangle.area(10,20)

print(result)

# With a static method we cannot instance into more objects
# But we can use instance variables.

