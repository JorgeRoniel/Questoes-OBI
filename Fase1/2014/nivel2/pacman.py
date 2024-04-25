#Aqui pegamos do usuario o tamanho do tabuleiro
tab = int(input())

jogadas = [] #definimos uma lista para guardar o conjunto de jogadas
jog = []
#aqui o usuario vai inserir a jogada, que vai ser guardada em 'jog', apos isso é guardada em jogadas
for i in range(tab):
    j = input()
    jog = list(j)
    jogadas.append(jog)

cont = 0 #definimos um contador, para contar quantos 'o' irão aparecer
l = [] #definimos essa lista para pegar os valores da variavel cont e depois pegar o maior

for i in range(len(jogadas)): #o primeiro for itera sobre as linhas da tabela
    if i % 2 == 0: #se o indice da linha for par, o segundo for ira percorrer as colunas da esq -> dir
        for j in range(len(jogadas)):
            if jogadas[i][j] == 'o': #se ele encontrar um 'o', então cont aumenta 1
                cont +=1
                if jogadas[i][j] == 'A': #Caso, depois dele achar um 'o', e depois vinher um A, ele adiciona cont na lista e depois zera ele
                    l.append(cont)
                    cont = 0
            elif jogadas[i][j] == 'A': #caso o elemento seja o 'A', então já faz o mesmo processo acima
                    l.append(cont)
                    cont = 0
    else:
        for j in range(len(jogadas)-1, 0-1, -1):# caso o indice da linha seja impar, ela é percorrida da dir -> esq
            if jogadas[i][j] == 'o':
                cont +=1
                if jogadas[i][j] == 'A':
                    l.append(cont)
                    cont = 0
            elif jogadas[i][j] == 'A':
                    l.append(cont)
                    cont = 0
l.append(cont) #add cont na lista

print(max(l))
