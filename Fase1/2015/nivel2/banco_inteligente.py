S = int(input())
qtd_notas = [int(n) for n in input().split()]

notas = [2, 5, 10, 20, 50, 100]

dp = [[0 for _ in range(S+1)] for _ in range(len(notas)+1)]
for i in range(len(notas)+1):
    dp[i][0] = 1


for i in range(1, len(notas)+1):
    for j in range(1, S+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, qtd_notas[i-1]+1):
            if j >= k*notas[i-1]:
                dp[i][j] += dp[i-1][j-k*notas[i-1]]

print(dp[len(notas)][S])
