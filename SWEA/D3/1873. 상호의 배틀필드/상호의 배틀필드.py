def up(board, x, y):
    # 범위를 벗어나거나, 벽이거나, 물일 때 이동 금지
    if x - 1 >= 0 and board[x-1][y] != '#' and board[x-1][y] != '*' and board[x-1][y] != '-':
        #if board[x-1][y] != '#' and board[x-1][y] != '*' and board[x-1][y] != '-':
        board[x][y] = '.'
        board[x - 1][y] = '^'
        return board, x - 1, y

    board[x][y] = '^'
    return board, x, y

def down(board, x, y):
    if x + 1 < H and board[x+1][y] != '#' and board[x+1][y] != '*' and board[x+1][y] != '-':
        board[x][y] = '.'
        board[x + 1][y] = 'v'
        return board, x + 1, y

    board[x][y] = 'v'
    return board, x, y

def left(board, x, y):
    if y - 1 >= 0 and board[x][y - 1] != '#' and board[x][y - 1] != '*' and board[x][y - 1] != '-':
        board[x][y] = '.'
        board[x][y - 1] = '<'
        return board, x, y - 1

    board[x][y] = '<'
    return board, x, y

def right(board, x, y):
    if y + 1 < W and board[x][y + 1] != '#' and board[x][y + 1] != '*' and board[x][y + 1] != '-':
        board[x][y] = '.'
        board[x][y + 1] = '>'
        return board, x, y + 1

    board[x][y] = '>'
    return board, x, y

def shoot(board, x, y):
    if board[x][y] == '>':
        for i in range(y + 1, W):
            if board[x][i] == '*':
                board[x][i] = '.'
                return board, x, y
            elif board[x][i] == '#':
                return board, x, y
    elif board[x][y] == '<':
        for i in range(y - 1, -1, -1):
            if board[x][i] == '*':
                board[x][i] = '.'
                return board, x, y
            elif board[x][i] == '#':
                return board, x, y
    elif board[x][y] == '^':
        for i in range(x - 1, -1, -1):
            if board[i][y] == '*':
                board[i][y] = '.'
                return board, x, y
            elif board[i][y] == '#':
                return board, x, y
    elif board[x][y] == 'v':
        for i in range(x + 1, H):
            if board[i][y] == '*':
                board[i][y] = '.'
                return board, x, y
            elif board[i][y] == '#':
                return board, x, y
    return board, x, y

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input().strip()) for _ in range(H)]
    N = int(input())
    command = input().strip()
    x, y = 0, 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == '^' or board[i][j] == 'v' or board[i][j] == '<' or board[i][j] == '>':
                x, y = i, j  # 전차 현재 위치 저장
                break

    for i in command:
        if i == 'U':
            board, x, y = up(board, x, y)
        elif i == 'D':
            board, x, y = down(board, x, y)
        elif i == 'L':
            board, x, y = left(board, x, y)
        elif i == 'R':
            board, x, y = right(board, x, y)
        elif i == 'S':
            board, x, y = shoot(board, x, y)

    print(f"#{test_case}", end=' ')
    for i in board:
        print(''.join(i))