
N = int(input())
M = int(input())
S = int(input())

achou = False
for i in range(M, N - 1, -1):
    soma = 0
    x = i
    while x > 0:
        soma += x % 10
        x //= 10
    if soma == S:
        achou = True
        resp = i
        break


'''
X = 6
soma = 0 + 6 = 6
x = 6 / 10 = 0
'''
if achou:
    print(resp)
else:
    print(-1)
