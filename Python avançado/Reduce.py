# Reduce
from functools import reduce # importe do Reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Exemplo de lista

def soma(x, y): # Funcao para passar os parametros necessarios
    return x + y

soma = reduce(soma, lista) # Funcao reduce sendo utilizada para somar todos os conteudos da lista
print(soma)
