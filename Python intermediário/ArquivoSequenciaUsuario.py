# Armazena a sequencia digitada pelo usuario
seq = input("Digite uma sequencia: ")

# Abre o arquivo ou cria se nao tiver um existente ele ja apaga o conteudo que tiver dentro e deixa em branco
arquivo = open("Arquivo", "w")

# Escreve um cabecalho e a sequencia digitada pelo usuario
arquivo.write("Sequencia digitada pelo usuario\n")
arquivo.write(seq)

#Fecha o arquivo
arquivo.close()

