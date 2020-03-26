languages = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separator = "; "

result = languages.split(separator) # Result is a list.

# new_string = "_".join(result)
new_string = separator.join(result)

print(new_string)


text = """Este es un texto 
con
saltos
de

linea"""

resultado = text.splitlines()

print(resultado)