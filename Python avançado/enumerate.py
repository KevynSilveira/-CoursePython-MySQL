# Exemplo sem enumerate

lista1 = ["abacaxi", "bola", "Cachorro"] # Cria a lista com o conteudo

for i in range (len(lista1)): # Lista os elementos e os indices a qual pertence
    print(i, lista1[i])

# Exemplo com enumerate

lista2 = ["abacaxi", "bola", "Cachorro", "Dado", "Elefante"] # Cria a lista com o conteudo

for i , nome in enumerate(lista2): # Exemplo de codigo utilizando enumerate
    print(i, nome)
