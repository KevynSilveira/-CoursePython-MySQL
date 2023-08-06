# Exemplo de codigo zip

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["abacaxi", "bola", "Cachorro", "Dado", "Elefante"]

for numero, nome in zip(lista1, lista2): # Concatena duas lista, podendo ser concatenada mais de duas lista
    print(numero, nome)