N = int(input())
pregos = input().split()

pregos_num = []
for p in pregos:
    num_p = int(p)
    pregos_num.append(num_p)

cruzamentos = 0
for i in range(N):
    for j in range(i+1, N):
        if(pregos_num[j] < pregos_num[i]):
            cruzamentos += 1

print(cruzamentos)