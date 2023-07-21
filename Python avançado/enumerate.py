# Exemplo sem enumerate

lista = ["abacaxi", "bola", "Cachorro"] # Cria a lista com o conteudo

for i in range (len(lista)): # Lista os elementos e os indices a qual pertence
    print(i, lista[i])

# Exemplo com enumerate

for i , nome in enumerate(lista): # Exemplo de codigo utilizando enumerate
    print(i, nome)
