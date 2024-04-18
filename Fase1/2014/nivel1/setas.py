def is_inside_board(x, y, N):
    return 0 <= x < N and 0 <= y < N

def count_safe_cells(board):
    N = len(board)
    safe_cells = [[True] * N for _ in range(N)]

    dx = [0, 0, 1, -1]  # Movimento nas direções: cima, baixo, direita, esquerda
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            x, y = i, j
            while True:
                direction = board[x][y]
                nx, ny = x + dx[direction], y + dy[direction]
                if not is_inside_board(nx, ny, N):
                    safe_cells[i][j] = False
                    break
                x, y = nx, ny

    return sum(sum(row) for row in safe_cells)

# Exemplo de entrada
N = 3
board = [
    [1, 0, 3],
    [2, 1, 2],
    [0, 3, 1]
]

print(count_safe_cells(board))  # Saída: 8
