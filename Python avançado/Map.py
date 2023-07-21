# Exemplo de map
def dobro(x): # Funcao para dobrar o valor do item passado
    return x*2
print(dobro(2))

valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista para dobrar o valor

valor_dobrado = map(dobro, valor) # Dobra o valor e salva em uma variavel

valor_dobrado = list(valor_dobrado) # Converte o arquivo para uma lista
print(valor_dobrado)
