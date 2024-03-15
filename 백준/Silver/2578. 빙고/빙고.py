import sys
input = sys.stdin.readline

board = [] #빙고판
num = [] #사회자가 부르는 수
for _ in range(5):
    board.append(list(map(int, input().split()))) #이중 리스트 생성
for _ in range(5):
    num += list(map(int, input().split()))

#가로 확인
def bingo_check():
    bingo = 0
    #가로 확인
    for i in board:
        if i.count(0) == 5:
            bingo += 1
    #세로 확인
    for i in range(5):
        y = 0
        for j in range(5):
            if board[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1
    #왼쪽위 대각선
    d1 = 0
    for i in range(5):
        if board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1
    #오른쪽위 대각선
    d2 = 0
    for i in range(5):
        if board[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1

    return bingo

cnt = 0  # 빙고 확인
# 빙고 게임 시작
for x in range(25):
    for i in range(5):
        for j in range(5):
            if num[x] == board[i][j]:
                board[i][j] = 0  # 사회자가 부르는 수는 0으로 만들기
                cnt += 1
    if cnt >= 12:
        res = bingo_check()
        if res >= 3:  # 빙고인지 아닌지 확인하기
            print(x + 1)
            break