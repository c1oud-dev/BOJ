'''
회문/팰린드롬
8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수

가로 확인 따로, 세로 확인 따로
'''
for tc in range(1, 11):
    length = int(input())
    board = [list(map(str, input())) for _ in range(8)] #리스트 컴프리헨션
    result = 0
    for i in range(8):
        j = 0
        while j + length <= 8:
            #가로
            row_word = ''.join(board[i][j:j + length]) #슬라이싱 결과 리스트
            reversed_row_word = row_word[::-1] #뒤집기
            if row_word == reversed_row_word:
                result += 1

            #세로
            column_word = ''.join([board[k][i] for k in range(j, j + length)])
            reversed_col_word = column_word[::-1]
            if column_word == reversed_col_word:
                result += 1
            j += 1

    print("#%d %s" %(tc, result))