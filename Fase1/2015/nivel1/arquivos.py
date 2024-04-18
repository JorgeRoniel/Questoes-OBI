#Aqui, pegamos o numero de arquivos e o numero maximo de pastas, conforme pede a questao
N, B = [int(n) for n in input().split()]

tamanhos = [int(i) for i in input('', end='').split() if int(i) <= B] #uma lista para cada arquivo

soma = 0 #uma variavel soma para dividir mais tarde com o tamanho maximo da pasta

#um for para somar os tamanhos de cada pasta
for tamanho in tamanhos:
    soma = soma + tamanho

totalPasta = soma/B #dividimos o valor da soma de cada pasta com o tamanho maximo das pastas
print(int(totalPasta)) #mostramos na tela o resultado final