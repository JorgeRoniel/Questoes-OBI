#pego os 4 comprimentos que são solicitados na questão
n1 = int(input("Digite o primeiro comprimento: "))
n2 = int(input("Digite o segundo comprimento: "))
n3 = int(input("Digite o terceiro comprimento: "))
n4 = int(input("Digite o quarto comprimento: "))

# verifico se ambos os comprimentos são menores que a soma dos outros tres
if n1 < (n2+n3+n4) and n2 < (n1+n3+n4) and n3 < (n1+n2+n4) and n4 < (n1+n2+n3):
    print("S") # caso seja, mostro na tela o 'S'
else:
    print("N")#caso não seja, mostro na tela o 'N'