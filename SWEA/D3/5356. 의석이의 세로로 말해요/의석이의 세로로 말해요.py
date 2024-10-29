'''
세로로 읽기

행 열 변환 하고 출력
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    board = [list(input().strip()) for _ in range(5)]
    #new_board = list(map(list, zip(*board)))  # 행 열 변환
    result = []
    for j in range(15):
        for i in range(5):
            if j < len(board[i]):
                result.append(board[i][j])
    print(f"#{test_case} {''.join(result)}")