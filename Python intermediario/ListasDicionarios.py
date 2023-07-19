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