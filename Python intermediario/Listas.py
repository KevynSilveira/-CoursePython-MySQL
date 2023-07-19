#Lista representa conjunto de dados em python

#numerica
numerica = [1,2,3,4,5,6,7,8,9,10]
palavras = ["nome", "idade", "endereco"]
misturada = ["nome", "idade", "endereco", 1, 2.3, 4, 5.6]

print(numerica, "\n", palavras)

#comeca no 0, entao o retorno sera 5
print(numerica[4])

#navegar entre na lista
for item in numerica:
    print(item)

#pega o tamanho da lista
tamanho = len(numerica)
print(tamanho)

#Para adicionar conteudo a lista:
numerica.append(11)
print(numerica)

#verifica se o parametro esta na lista
if 7 in numerica:
    print("esta na lista")

#apaga tudo na lista do 7 em diante
del numerica[7:]
print(numerica)

#ordenando lista
lista = [546545, 1454564, 1545, 54, 6, 48, 5, 4, 54778, 1213, 8797, 14752, 1, 2, 3, 45, 5, 6]
lista1= [546545, 1454564, 1545, 54, 6, 48, 5, 4, 54778, 1213, 8797, 14752, 1, 2, 3, 45, 5, 6]
lista.sort()#ordena a propria lista passada
lista1 = sorted(lista)#ordena a lista, porem necessita atribuir ela a uma variavel
print(lista)
print(lista1)
