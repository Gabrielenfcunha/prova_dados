from Livros import Livros
from Pilha import PilhaLivros
from Pilha import PilhaRevistas
l1 = PilhaLivros()
r1 = PilhaRevistas()
def menu():

    teclado = input( '''
    Publicação pilha :
    1- Adicionar pilha Livros
    2- Remover pilha Livros
    3- Adicionar pilha Revista
    4- Remover pilha Revista
    5- imprimir pilha Livros 
    6- imprimir pilha Revista

     >>>: '''
    )
    if teclado == "0": return
    if teclado == "1":
      l1.addLivros()
    if teclado == "2":
      l1.removerLivros()
    if teclado == "3":
      r1.addrevistass()
    if teclado == "4":
      r1.removerRvista()
    if teclado == "5":
      l1.imprimirLivros()     
    if teclado == "6":
      r1.imprimirRevista()


    menu() 

menu()