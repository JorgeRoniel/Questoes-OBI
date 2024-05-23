d = int(input())
a = int(input())
n = int(input())

# vamos usar chegada para calcular o valor da diária
chegada = n
if chegada > 15:
    chegada = 15

diaria = d + (chegada-1)*a

'''
d = 100
a = 20
n = 15

cheg = 15

diaria = 100 + 14*20 = 380

31 - 15 + 1 = 17

17 * 380 = 6460
'''

print((31 - n + 1)*diaria)
