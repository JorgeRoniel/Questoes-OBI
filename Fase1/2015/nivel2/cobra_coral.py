#pegamos os quatro valores solicitados pela questão
n1,n2,n3,n4 = map(int, input().split())


if n1 == n3 and n2 != n4:
    print("V")  
elif n1 != n3 and n2 == n4:
    print("V")
else:
    print("F")