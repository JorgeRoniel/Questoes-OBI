def is_triangulo(a, b ,c):
    if a < (b+c) and b < (a+c) and c < (b+a):
        return True
    return False


#pego os 4 comprimentos que são solicitados na questão
n1, n2, n3, n4 = [int(n) for n in input().split()]

if (is_triangulo(n1, n2, n3) or 
is_triangulo(n1, n2, n4) or 
is_triangulo(n1, n3, n4) or 
is_triangulo(n2, n3, n4)):
    print('S')
else:
    print('N')