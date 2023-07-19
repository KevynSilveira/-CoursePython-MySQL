# Abre o arquivo para manipulacao e armazena dentro da variavel meu_arquivo1
meu_arquivo1 = open("meu arquivo.txt")

# Le as linhas e adiciona na variavel linha em formato de lista
linhas = meu_arquivo1.readlines()
print(linhas)

# Abre o arquivo para manipulacao e armazena dentro da variavel meu_arquivo2
meu_arquivo2 = open("Meu arquivo.txt")

#armazena o texto completo dentro da variavel
texto_completo = meu_arquivo2.read()
print(texto_completo)