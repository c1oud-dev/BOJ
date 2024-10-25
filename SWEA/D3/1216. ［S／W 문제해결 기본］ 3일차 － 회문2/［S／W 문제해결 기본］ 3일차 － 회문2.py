'''
100 * 100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제
'''
def palindrome(board):
    length, max_len = 0, 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                word_slice = board[i][j:j + k]

                if word_slice == word_slice[::-1]:
                    length = len(word_slice)

                if max_len < length:
                    max_len = length
    return max_len

for _ in range(10):
    test_case = int(input())
    board = [input().strip() for _ in range(100)]
    row_len = palindrome(board)
    #행 열 변환
    new_board = [list(i) for i in zip(*board)]
    col_len = palindrome(new_board)
    if row_len > col_len:
        result = row_len
    else:
        result = col_len

    print(f"#{test_case} {result}")