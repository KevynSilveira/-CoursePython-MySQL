a = 2
b = 0

# Exemplo de erro, divisao por 0

# print(a/b)

try: # Tentativa de execucao de codigo
    print(a/b)
except: # Tratamento de excecao
    print("Nao e permitido a divisao por 0")