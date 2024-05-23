MAX = 10**6
N = int(input())
S = int(input())

vetor = [int(x) for x in input().split()]
resp = 0

freq = [0 for i in range(MAX)]
'''
Inicializa uma lista de frequências freq com tamanho MAX, onde cada elemento é 
inicializado como 0. Essa lista será usada para contar o número de intervalos 
com determinada soma.

'''
soma = 0
freq[0] = 1

for v in vetor:
    soma += v #Adiciona o valor do elemento atual à variável soma, atualizando a soma acumulada dos elementos do vetor

    if soma - S >= 0: #Verifica se a diferença entre a soma atual (soma) e S é maior ou igual a zero. Isso indica que encontramos um intervalo com soma igual a S.

        resp += freq[soma - S] #Adiciona à resposta o número de vezes que a soma atual menos S aparece nos intervalos anteriores. Isso é feito acessando a lista de frequências freq.

    freq[soma] += 1 #Incrementa a frequência da soma atual na lista de frequências freq, indicando que encontramos mais um intervalo com essa soma.

'''
N = 6
S = 2
resp = 6

vetor = [0, 2, 0, 1, 0, 1]
freq = [2, 0, 2, 2, 1, 0, 0, 0, 0, 0]

soma = 4

v = 1

'''
print(resp)


