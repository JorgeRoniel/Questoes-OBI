'''
Se o nó atual (atual) ainda não foi visitado (visitados[atual] == False):
Marca o nó como visitado (visitados[atual] = True).

O código então percorre todos os vizinhos do nó atual (for vizinho in adjacencias[atual]:).
Se um vizinho ainda não foi visitado (visitados[vizinho] == False), a função dfs é chamada 
recursivamente para explorar esse vizinho.
'''

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

'''
adjacencias: Um dicionário que será usado para armazenar o grafo,
onde cada estudante é uma chave e seu valor é uma lista de estudantes 
conectados.
'''
adjacencias = {i: [] for i in range(1, n+1)}

'''
visitados: Um dicionário que marca se cada 
estudante foi visitado (False inicialmente para todos).
'''
visitados = {i: False for i in range(1, n+1)}

for i, j in l:
    adjacencias[i].append(j)
    adjacencias[j].append(i)

num_times = 0
for estudantes in range(1, n+1):
     if visitados[estudantes] == False:
          dfs(adjacencias, estudantes, visitados)
          num_times += 1

print(num_times) #mostra quantos times é possivel ser montados.