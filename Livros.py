from Publicacao import Publicacao

class Livros(Publicacao):
    def __init__(self, id = None, data = None,titulo = None, autor = None):
        super().__init__(id=id, data=data)
        self.titulo = titulo
        self.__autor = autor
        self.proximo = None
    

    def cadastrar(self, id, data,titulo, autor):
        self.id = id
        self.data = data
        self.titulo = titulo
        self.__autor = autor


    def getautor(self):
        return self.__autor

    def setautor(self, autor):
        self.__autor = autor   

    def getInformacoes(self):
        return super().getInformacoes() + f"\nTitulo:{self.titulo}\nAutor: {self.__autor}"