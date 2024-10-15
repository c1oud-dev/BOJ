'''
영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.
총 5줄이지만 각 줄은 가변적이다.
'''

letters = [input() for i in range(5)]
for j in range(15): #행의 길이
    for i in range(5): #열
        if j < len(letters[i]): #길면 출력 안 함
            print(letters[i][j], end='')