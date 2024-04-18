#Aqui, pegamos o numero de arquivos e o numero maximo de pastas, conforme pede a questao
N, B = [int(n) for n in input().split()]

tamanhos = [int(i) for i in input().split() if int(i) <= B] #uma lista para cada arquivo
tamanhos.sort()
soma = 0 #uma variavel soma para dividir mais tarde com o tamanho maximo da pasta

#um for para somar os tamanhos de cada pasta
i = 0 
j = len(tamanhos) - 1
while j > i:
    if tamanhos[i] + tamanhos[j] <= B:
        i += 1
    soma += 1
    j -= 1

if i == j:
    soma += 1    

#dividimos o valor da soma de cada pasta com o tamanho maximo das pastas
print(soma)#mostramos na tela o resultado final