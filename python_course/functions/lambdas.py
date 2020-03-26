# Normal functions
'''
def celsius_to_fahrenheit(degrees):
    return degrees * 1.8 + 32

function_variable = celsius_to_fahrenheit
result = function_variable(32)
print(result)
'''
# Lambda function

lambda_function = lambda degrees=0 : degrees * 1.8 + 32

result = lambda_function(32)

print(result)

# Examples:

'''
sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
'''