N = int(input()) #pegamaos o numero de pregos
pregos = input().split() #pegamos a ordem na linha horizontal dos pregos

#Aqui convertemos os valores da lista para inteiros
pregos_num = []
for p in pregos:
    num_p = int(p)
    pregos_num.append(num_p)

cruzamentos = 0 #Uma variavel para contar os cruzamentos

'''
Basicamente, vamos percorrer a lista, e para cada valor, verificamos se ele cruza com 
os outros numeros, por exemplo, se pegarmos o 5, verificamos se os numeros afrente dele na lista são 
menores que ele, caso sejam, há um cruzamento. Assim, cada numero é analisado.

'''
for i in range(N):
    for j in range(i+1, N):
        if(pregos_num[j] < pregos_num[i]):
            cruzamentos += 1

'''
N = 6
pregos_num = [1, 5, 3, 4, 6, 2]
cruzamentos = 3

i = 2
j = 3

4 < 3
'''

print(cruzamentos)