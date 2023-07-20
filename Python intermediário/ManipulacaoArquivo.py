# Abre o arquivo para manipulacao e armazena dentro da variavel meu_arquivo1
meu_arquivo1 = open("meu arquivo.txt")

# Le as linhas e adiciona na variavel linha em formato de lista
linhas = meu_arquivo1.readlines()
print(linhas)
# Fecha o arquivo de texto aberto
meu_arquivo1.close()

# Abre o arquivo para manipulacao e armazena dentro da variavel meu_arquivo2
meu_arquivo2 = open("Meu arquivo.txt")

#armazena o texto completo dentro da variavel
texto_completo = meu_arquivo2.read()
print(texto_completo)
# Fecha o arquivo de texto aberto
meu_arquivo2.close()

# Cria um novo arquivo de texto com o nome Meu arquivo3, ou se ja tiver um existente com esse nome
# ele apaga tudo e deixa em branco
meu_arquivo3 = open("Meu arquivo3.txt", "a")

#Escreve no arquivo aberto
meu_arquivo3.write("Essa e a cricao de um novo arquivo de texto utilizando a funcao write")

# Fecha o arquivo de texto aberto
meu_arquivo3.close()