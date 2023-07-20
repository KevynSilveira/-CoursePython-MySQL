menu = 0

def abrir_arquivo(): # Abri o arquivo digitado pelo usuario
    nome_arquivo = input("Digite o arquivo a ser aberto: \n")
    arquivo = open(nome_arquivo)
    return arquivo

def ler_arquivo(arquivo): # Faz a leitura do arquivo aberto
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())

# Inicia um while de repeticao
while menu != 3:

    #Printa um menu para escolha de opecao
    print("(1) Abrir arquivo\n"
          "(2) Ler arquivo aberto\n"
          "(3) Fechar programa\n")

    escolha = int(input("Digite a opcao desejada:"))

    # Abri o arquivo
    if escolha == 1:
        arquivo = abrir_arquivo()
    # Le o arquivo aberto
    elif escolha == 2:
        ler_arquivo(arquivo)

    # Fecha o while
    elif escolha == 3:
        print("voce saiu do programa!")
        menu = 3

    # Opcao invalida, da um retorno e volta para looping
    else:
        print("Digite uma opcao valida!")

