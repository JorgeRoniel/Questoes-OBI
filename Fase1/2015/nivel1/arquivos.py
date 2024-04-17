#Aqui, pegamos o numero de arquivos e o numero maximo de pastas, conforme pede a questao
numero_arquivos = int(input("Digite o numero de arquivos: "))
tamanho_pasta = int(input("Digite o tamanho maximo das pastas: "))

tamanhos = [] #uma lista para cada arquivo

#aqui, utiizamos um loop para pegar o tamanho individual de cada arquivo
for i in range(numero_arquivos):
    n = int(input("Digite o tamanho do arquivo: "))
    tamanhos.append(n)

soma = 0 #uma variavel soma para dividir mais tarde com o tamanho maximo da pasta

#um for para somar os tamanhos de cada pasta
for tamanho in tamanhos:
    soma = soma + tamanho

totalPasta = soma/tamanho_pasta #dividimos o valor da soma de cada pasta com o tamanho maximo das pastas
print(totalPasta) #mostramos na tela o resultado final