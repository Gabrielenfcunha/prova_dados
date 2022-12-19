from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, id, data):
        self.id = id
        self.data = data

    @abstractmethod
    def cadastrar(self, id, data):
        pass

    def getInformacoes(self):
        return f"id: {self.id}\nData Publicaçao: {self.data}"