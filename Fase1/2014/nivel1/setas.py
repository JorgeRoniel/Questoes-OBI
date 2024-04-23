N = int(input())
board = [['*' for _ in range(N+2)] for _ in range(N+2)]
soma = 0

def is_inside_board(x, y, N):
    return 0 <= x < N+1 and 0 <= y < N+1

def solucao(i, j):
    if board[i][j] == 's' or board[i][j] not in ['>', '<', 'A', 'V']:
        return board[i][j]
    
    dx = [0, 0, 1, -1]  # Movimento nas direções: cima, baixo, direita, esquerda
    dy = [1, -1, 0, 0]
    global soma

    x, y = i, j
    direction = 0
    letras = board[i][j]
    if letras == '>':
        direction = 0
    elif letras == '<':
        direction = 1
    elif letras == 'V':
        direction = 2
    elif letras == 'A':
        direction = 3
                    
    x, y = x + dx[direction], y + dy[direction]
    if is_inside_board(x, y, N):
        board[i][j] = 's'
    else:
        board[i][j] = '*'
    board[i][j] = solucao(x, y)

    if board[i][j] != 's' and board[i][j] not in ['>', '<', 'A', 'V']:
        soma +=1
    return board[i][j]

for c in range(N+2):
    board[0][c] = '*'

for i in range(1, N+1):
    l = input()
    linha = list(l)
    board[i][0] = '*'
    for j in range(N):
        board[i][j+1] = linha[j]
    board[i][N+1] = '*'

for x in range(N+2):
    board[N+1][x] = '*'

for i in range(1, N+1):
        for j in range(1, N+1):
            solucao(i, j)
            
print((N*N)-soma)
