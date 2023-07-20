import random

#Ira escolher um numero aleatorio entre 0 e 10.
numero = random.randint(0, 10)
print(numero)

#deixa o numero fixo a apenas um resultado pixo
# random.seed(1)
numero2 = random.randint(0,10)
print(numero2)

# Recebe como padrao um lista para escolher o numero aleatorio
lista = [1, 2, 3, 4]
numero3 = random.choice(lista)
print(numero3)