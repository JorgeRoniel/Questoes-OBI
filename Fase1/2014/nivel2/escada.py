N, M = map(int, input().split()) #pegamos as dimensões da matriz
ans = 'S' #definimos que por padrão, a matriz está no formato correto

lastc = -1 
for i in range(N):
    flag = 1
    c = 0
    row = list(map(int, input().split())) # pegamos cada valor e guardamos em uma lista
    for m in row: #para cada valor valor nessa lista
        if m == 0 and flag: #se o valor for igual a zero e a flag for 1, a variavel c é incrementada
            c += 1 #essa variavel conta os zeros na linha
        else: #Caso não seja, flag recebe zero.
            flag = 0
    if c < M and c < lastc: #Se o c for menor que o numero de colunas e for menor que o numeros de zeros da coluna acima
        ans = 'N' #a variavel não está na forma correta
        break
    lastc = c #a variavel 'lastc' recebe o numeros de zeros que tiveram nessa linha, que será a linha anterior


'''
N = 4
M = 6

[1, 2, 9, 9, 9, 9]
[0, 0, 3, 9, 9, 9]
[0, 0, 0, 0, 5, 9]
[0, 0, 0, 0, 0, 6]

lastc = -1
flag = 0
c = 0

'''

print(ans)
