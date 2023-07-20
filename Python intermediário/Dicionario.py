# Criando um dicionario

# Um dicionario e identificado pois utiliza chaves na sua criacao e tem um padrao
# para criacao da seguinte maneira primeiro indica o valor a ser armazena, cooloque
# dois pontos : e sem seguida entre aspas tambem coloque o valor a ser armazenado dentro
# daquele indique adicionado anteriormente

meu_dicionario = {
    "A":"Ameixa",
    "B":"Bola",
    "C":"Casa"
}
# Chama o print e passa o indice que deseja chamar
print(meu_dicionario["B"])


# Navegando dentro do dicionario

# Lista todos os valores armazenas, porem nao o indice ao qual foi declado
for chave in meu_dicionario:
    print(meu_dicionario[chave])

# Lista todos os itens (indice e conteudo)
for i in meu_dicionario.items():
    print(i)

# Listando os indice
for i in meu_dicionario.keys():
    print(i)

# Listando os valores
for i in meu_dicionario.values():
    print(i)