valor1 = int(input("Digite o primeiro numero? "))
valor2 = int(input("Digite o segundo numero? "))

conclui_operacao = True
resultado = 0

while conclui_operacao:
    sinal = input("Digite um sinal: ")

    if sinal == "/":
        resultado = valor1 / valor2
        conclui_operacao = False
    elif sinal == "*":
        resultado = valor1 * valor2
        conclui_operacao = False
    elif sinal == "+":
        resultado = valor1 + valor2
        conclui_operacao = False
    elif sinal == "-":
        resultado = valor1 - valor2
        conclui_operacao = False
    else:
        print("Escolha uma operacao valida!")

print(resultado)