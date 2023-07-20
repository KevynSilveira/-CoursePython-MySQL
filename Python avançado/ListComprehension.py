# Exemplo de codigo sem listComprehension
x = [1, 2, 3, 4] # Cria uma lista
y = []

for i in x: # Faz um for para passar em todos as variavel da lista e elevar elas a 2
    y.append(i**2)

print(x)
print(y)


a = [1, 2, 3, 4, 5] # Cria uma lista
b = [i**2 for i in a] # exemplo de listComprehension
c = [i for i in a if i%2==1]

print(b)
print(c)
