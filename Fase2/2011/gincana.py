def dfs(adjacencias, no, visitados):
    atual = no
    if visitados[atual] == False:
        visitados[atual] = True
        for vizinho in adjacencias[atual]:
            if visitados[vizinho] == False:
                    dfs(adjacencias, vizinho, visitados)

n, m = [int(i) for i in input().split()]
l = []
for x in range(m):
    alunos = [int(num) for num in input().split()]
    l.append(alunos)

adjacencias = {i: [] for i in range(1, n+1)}
visitados = {i: False for i in range(1, n+1)}

for i, j in l:
    adjacencias[i].append(j)
    adjacencias[j].append(i)

num_times = 0
for estudantes in range(1, n+1):
     if visitados[estudantes] == False:
          dfs(adjacencias, estudantes, visitados)
          num_times += 1

print(num_times)