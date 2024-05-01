n, m = map(int, input().split()) #pega quantas gerações e quantos foram na festa

geracoes = [[] for _ in range(n+1)] #faz uma lista de listas vazias para registar as gerações
pais = list(map(int, input().split())) #pega os pais, segunda linha da entrada
for childid, parentid in enumerate(pais, 1):
    geracoes[parentid].append(childid) #preenche a lista com as gerações

visitados = [False] * (n+1) #criamos uma lista pra registrar os nós ja visitados
lista_comp = list(map(int, input().split())) #pegamos os descendentes que foram a festa
for id in lista_comp:
    visitados[id] = True #na lista visitados tem tudo falso, nos ids que forem iguais ao numero na lista_comp, ele marca true

'''
Agora, vamos utilizar o algoritmo de busca DFS, que serve para contar a distancia de cada nó para o nó raiz,
para isso, fazemos duas listas inicializadas com 0, uma para contar as distancias e outra para contar a 
ocorrencia dos descendentes que foram a festa
'''
cont_dist, gencomp = [0] * (n+1), [0] * (n+1) 

def dfs(v, dist):
    cont_dist[dist] += 1 #aqui marcamos a distancia, nos index que representam os nós
    if visitados[v]:
        gencomp[dist] += 1 #marcamos a presença das gerações

    for son in geracoes[v]: #para cada filho na lista gerações, 
        dfs(son, dist+1) #o proximo nó é acessado, e a distancia acrescentada

dfs(0, 0) #começamos no nó raiz

for d in range(1, n+1):
    if cont_dist[d] == 0:
        break
    if d > 1:
        print(" ")
    print("%.2f" % (100.0 * gencomp[d] / cont_dist[d]), end='' ) #calculamos a porcentagem
print('\n')