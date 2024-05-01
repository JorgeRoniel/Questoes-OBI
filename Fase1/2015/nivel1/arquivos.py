#Aqui, pegamos o numero de arquivos e o numero maximo de pastas, conforme pede a questao
N, B = [int(n) for n in input().split()]

tamanhos = [int(i) for i in input().split() if int(i) <= B] #uma lista para cada arquivo
tamanhos.sort()
soma = 0 

i = 0 
j = len(tamanhos) - 1
while j > i:
    if tamanhos[i] + tamanhos[j] <= B:
        i += 1
    soma += 1
    j -= 1

if i == j:
    soma += 1    

print(soma)#mostramos na tela o resultado final