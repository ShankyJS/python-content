# # Function without parameter limit.
# def sum(parameter_required, *args):
#     total = 0
#     print(parameter_required)
#     for valor in args:
#         total += valor
#     return total
# result = sum("This is a required argument", 10, 20, 30, 40, 50, 60)
# print(result)

# def authenticated_users(**kwargs):
#     print(kwargs)
# authenticated_users(codi=True, facilito=False)


def combination(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)

combination("Required value", 10, 20, value_one=True, value_two=False )
