class Person():
#variables de clase
    edad: int = 20
    def __int__(self,
                name,
                nationality): #variables de instancia

        self.name = name
        self.nationality = nationality

    def GoodBye(self, name):
        print('Bye, ', name)

    @classmethod
    # Definimos un método de clase
    def Hello(cls, name):
        print('hola, ', name)

    @staticmethod
    def Walk():
        print('Walking')


class Book():
    def __init__(self, autor, name, pages):
        self.autor = autor
        self.name = name
        self.pages = pages

    #Este es el método que va a llamarse cuando querramos impprimir una instancia de clase
    def __str__(self):
        return f'{self.name} writing by {self.autor}. this book have {self.pages} pages'

    def __del__(self):
        print(f'Se ha eliminado el libro {self.name}')

myBook = Book('Lovercraft', 'Mites', 69)
print(myBook)
del myBook

class Circle():
    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        return 3.1416*(self.radio**2)

myCircle = Circle(15)
print(myCircle.area)
