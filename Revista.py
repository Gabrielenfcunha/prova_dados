from Publicacao import Publicacao

class Revistas(Publicacao):
    def __init__(self, id=None, data=None, preco= None):
        super().__init__(id=id, data=data)
        self._preco = preco
        self.prox = None

    def getInformacoes(self):
        return super().getInformacoes() + f"\npreco: {self._preco}"

    def cadastrar(self, id, data, preco):
        self.id = id
        self.data = data
        self._preco = preco
