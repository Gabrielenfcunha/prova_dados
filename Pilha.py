from Livros import Livros
from Revista import Revistas


class PilhaLivros:
    def __init__(self):
        self.toppoLivros = None
       

    def addLivros(self):
        id = int(input('Digite id seu Livro: '))
        data = input('Digite a data Publicaçao Livro: ')
        Titulo = input('Digite a Titulo do Livro: ')
        autor = input('Digite a autor do seuLivro: ')
        Livro = Livros(id,data,Titulo,autor) 
        if self.toppoLivros == None:
            self.toppoLivros = Livro
        else:
            Livro.proximo = self.toppoLivros
            self.toppoLivros = Livro
        self.imprimirLivros()

    def imprimirLivros(self):
        if self.toppoLivros == None:
            print("Pilha de Livros vazia!\n------------")
        else:
            print("------------\n")
            texto = " "
            aux = self.toppoLivros
            while (aux):
                texto += str(aux.getInformacoes()) + " |\n " 
                aux = aux.proximo
                print(texto)

                
    def removerLivros(self):
        if self.toppoLivros == None:
            print("Pilha vazia\n-------------")
        else:
            self.toppoLivros = self.toppoLivros.proximo
        self.imprimirLivros()

class PilhaRevistas:
    def __init__(self):
        self.topoRevista = None  

    def addrevistass(self):
        id = int(input('Digite id  Revista: '))
        data = input('Digite a data Publicaçao do Revista: ')
        preco = int(input('Digite a preco do Revista: '))
        revistass = Revistas(id,data,preco)
        if self.topoRevista == None:
            self.topoRevista = revistass
        else:
            revistass.prox = self.topoRevista
            self.topoRevista = revistass
        self.imprimirRevista()

    def imprimirRevista(self):
            if self.topoRevista == None:
                print("Pilha de revista vazia!\n------------")
            else:
                print("------------\n")
                texto = " "
                res = self.topoRevista
                while (res):
                  texto +=  "\nId: " + str(res.id )+ ": " + "\nData: " + res.data + "\nPreço: " + str(res._preco) + " |\n " 
                  res = res.prox
                  print(texto)
                  
    def removerRvista(self):
        if self.topoRevista == None:
            print("Pilho vazia\n-------------")
        else:
            self.topoRevista = self.topoRevista.prox
        self.imprimirRevista()
