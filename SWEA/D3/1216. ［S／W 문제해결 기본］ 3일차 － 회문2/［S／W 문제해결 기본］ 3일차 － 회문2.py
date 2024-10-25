'''
100 * 100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제
'''
def palindrome(board):
    max_len = 0
    for i in range(100):
        for j in range(100):
            for k in range(100, 0, -1): #큰 길이부터 시작하여 검사
                if j + k <= 100:
                    word_slice = board[i][j:j + k]

                    if word_slice == word_slice[::-1]: # 회문 확인
                        max_len = max(max_len, k) # 최대 길이 갱신
                        break # 최대 길이 찾았으므로 더 짧은 길이는 검사하지 않음
    return max_len

for _ in range(10):
    test_case = int(input())
    board = [input().strip() for _ in range(100)]
    row_len = palindrome(board)
    #행 열 변환
    new_board = [list(i) for i in zip(*board)]
    col_len = palindrome(new_board)
    result = max(row_len, col_len)

    print(f"#{test_case} {result}")