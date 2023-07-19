nome = input("Qual seu nome? ")
nota1 = int(input("Digite a primeira nota? "))
nota2 = int(input("Digite a segunda nota? "))
resultado = (nota1 + nota2) / 2
if resultado >= 6:
    print(nome + f" parabéns,você tirou {resultado} e foi aprovado!")
else:
    print(nome + f" infelizmente você tirou {resultado} e foi reprovado!")

