MAX = 200000 #numero maximo estabelecido pela questão
N = int(input()) #pegamos do usuario o numero de peças a ser usado

#Inicializamos a lista de letras e a listas dos numeros que estão a direita
letra = [0 for i in range(MAX+1)] 
direita = [0 for i in range(MAX+1)]

for i in range(N):
    I = input().split() #Aqui recebemos as peças inseridas pelo usuario, a função split divide a entrada e guarda no I como uma lista
    E = int(I[0]) #O 'E' representa o numero que fica a esquerda, então pegamos o valor que esta na posição 0 do I
    letra[E] = I[1] #A lista letra na posição 'E', que é o numero que fica a esquerda, recebe o valor que esta na posição 1 de 'I'
    direita[E] = int(I[2]) #A lista direita recebe o elemento que esta na posição 2 de 'I'

#Aqui vamos printar na tela a palavra formada
E = 0
while E != 1: 
    print(letra[E])
    E = direita[E]