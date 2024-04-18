#pegamos os quatro valores solicitados pela questão
n1, n2, n3, n4 = [int(n) for n in input().split()]


soma = n1+n2+n3+n4 #fazemos a soma

#caso a soma seja maior ou igual a vinte, a cobra coral é verdadeira, senão é falsa.
if soma >= 20:
    print("V")
else:
    print("F")