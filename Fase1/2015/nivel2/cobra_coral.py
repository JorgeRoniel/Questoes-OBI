#pegamos os quatro valores solicitados pela questão
n1 = int(input("Digite o primeiro num: "))
n2 = int(input("Digite o segundo num: "))
n3 = int(input("Digite o terceiro num: "))
n4 = int(input("Digite o quarto num: "))


soma = n1+n2+n3+n4 #fazemos a soma

#caso a soma seja maior ou igual a vinte, a cobra coral é verdadeira, senão é falsa.
if soma >= 20:
    print("V")
else:
    print("F")