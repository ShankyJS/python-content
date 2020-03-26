# Nomenclatura: Cammel case (inicial Mayuscula y las demas minuscula)
class User:

    def __init__(self, username='', mail='', name=''):
        self.username = username
        self.mail = mail
        self.name = name

    def wave(self):
        return "Hello, I'm a user " + self.name

    def show_username(self):
        print(self.username)

    def show_name(self):
        print(self.name)


# Instance of the class (creating an object)
codigo = User("Codigo", "codigo@codigofacilito.com", "Codigo")

facilito = User()

result = codigo.wave()

print(result)
