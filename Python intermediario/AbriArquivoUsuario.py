# Pede o nome do arquivo para o usuario
nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")

# Abre o arquivo escrito pelo usuario
arquivo = open(nome_arquivo)

#armazena seu conteudo em uma lista
lista = arquivo.readlines()

# Imprimi todo o conteudo da lista
for linha in lista:
    print (linha.strip()) #Tira o espacamento entre linhas