#Primeira maneira mais simples

#lista = [3,2,1]
#lista = sorted(lista)
#print(lista)

#Segunda maneira

lista = [877,1,5456]
for i in range(len(lista)):
    menor = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j

    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)