def square(number):
    return number * number


number_list = [1, 2, 3, 4, 5, 100]
result = map(square, number_list)

list_result = list(result)
print(list_result)


# Lambda function

lambda_list = [1,2,3,4,5,6]
lambda_result = map(lambda number: number * number , lambda_list)

lambda_list_result = list(lambda_result)
print(lambda_list_result)