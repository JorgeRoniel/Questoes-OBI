#Aqui pegamos do usuario o tamanho do tabuleiro
tab = int(input())

jogadas = [] #definimos uma lista para guardar o conjunto de jogadas
jog = [] #definimos outra lista para guardar cada jogada

#aqui o usuario vai inserir a jogada, que vai ser guardada em 'jog', apos isso é guardada em jogadas
for i in range(tab):
    jog = input().split()
    jogadas.append(jog)

cont = 0 #definimos um contador, para contar quantos 'o' irão aparecer

for jogada in jogadas: #acesso cada jogada em jogadas
    for letra in jogada: #acesso o conteudo de cada jogada

        #Aqui, verifico se na linha contem um "A", pois quando a linha tem um "A", ela não vale para 
        #a contagem.
        if 'A' in letra:
            cont = cont
        
        #caso não tenha o "A", vamos verificar cada elemento, e toda vez que tiver o "o", cont aumenta mais 1.
        else:
            for i in letra:
                if i == 'o':
                    cont += 1

print(cont) #mostra na tela o numero de "o", como pedido na questão.