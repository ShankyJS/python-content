courses = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]

# course = courses[10]
# print(course)

# Creating a new list with the last one
#var    list  from:to:jumps
sub = courses[1:7:2]
print(sub)

reverse_list = courses[::-1]
print (reverse_list)


'''
[:] Todos los elementos.
[start:] Todos los elementos desde el índice establecido(start).
[:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
[start:end] Todos los elementos de un rango de índices.
[start:end:step] Todos los elementos de un rango de índices con saltos.
De igual forma, este listado es aplicable a las tuplas y los strings.
'''