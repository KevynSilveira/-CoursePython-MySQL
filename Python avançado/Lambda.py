# Exemplo de Lambda, utilizada para fazer o trabalho de uma funcao, porem e executada uma unica vez
valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista para dobrar o valor

valor_dobrado = map(lambda i: i*2, valor) # Dobra o valor e salva em uma variavel

valor_dobrado = list(valor_dobrado) # Converte o arquivo para uma lista
print(valor_dobrado)
