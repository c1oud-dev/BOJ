'''
100*100 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라
'''
def calc(board):
    max_sum = 0
    for i in range(100):
        sum_num = sum(board[i][:])  # 0~99 인덱스의 전체 합 구하기
        max_sum = max(sum_num, max_sum)  # 합계의 최댓값 구하기
    return max_sum

def diagonal(board):
    right_sum, left_sum = 0, 0
    for i in range(100):  # 오른 대각
        right_sum += board[i][i]
        left_sum += board[i][9 - i]
    return max(right_sum, left_sum)

for _ in range(10):
    test_case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    row_max = calc(board)  # 행의 합
    # 행 열 변환 후 열의 합
    new_board = list(map(list, zip(*board)))
    col_max = calc(new_board)
    # 대각선 최댓값
    dia_max = diagonal(board)
    result = max(row_max, col_max, dia_max)
    print(f"#{test_case} {result}")
