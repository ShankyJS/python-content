number = 123456789
counter = 0

while number >= 1:
    counter+=1
    number = number / 10
else:
    print("The quantity of digits of the number is ", counter)