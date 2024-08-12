from collections import deque

'''
A função bfs é usada para explorar 
todos os vértices que pertencem ao mesmo componente conexo, 
começando de um vértice inicial "start".
'''

def bfs(start, visitado, adj):
    fila = deque([start])
    visitado[start] = True
    
    while fila:
        node = fila.popleft()
        for vizinho in adj[node]:
            if not visitado[vizinho]:
                visitado[vizinho] = True
                fila.append(vizinho)

'''
Para cada vértice não visitado, inicia-se uma nova BFS, o que indica que 
encontramos uma nova família. O contador familias é incrementado para cada 
componente conexo encontrado.
'''

def contar_familias(N, relacionamentos):
    # Criar a matriz de adjacência

    '''
    adj é uma lista de listas, 
    onde adj[i] contém todos os vértices que 
    estão conectados ao vértice i.
    '''
    
    adj = [[] for _ in range(N+1)]
    
    for a, b in relacionamentos:
        adj[a].append(b)
        adj[b].append(a)
    
    visitado = [False] * (N + 1)
    familias = 0
    
    # Realizar BFS para encontrar todos os componentes conexos
    for i in range(1, N + 1):
        if not visitado[i]:
            bfs(i, visitado, adj)
            familias += 1
    
    return familias

# Leitura dos dados de entrada
N, M = map(int, input().split())
relacionamentos = [tuple(map(int, input().split())) for _ in range(M)]

# Contar o número de famílias
resultado = contar_familias(N, relacionamentos)

# Exibir o resultado
print(resultado)
