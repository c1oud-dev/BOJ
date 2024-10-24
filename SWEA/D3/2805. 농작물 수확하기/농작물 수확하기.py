'''
n * n 크기의 농장이 있다. 다음과 같은 규칙이 있다.
1. 농장의 크기는 항상 홀수이다.
2. 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
이렇게 해서 얻을 수 있는 수익은 얼마인지 구하여라.
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input()) #농장 크기
    farm = [list(map(int, input())) for _ in range(n)] #정수이므로 리스트로 받기
    result = 0
    start, end = n // 2, n // 2

    for i in range(n):
        for j in range(start, end + 1):
            result += farm[i][j]
        if i < n // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#%d %d" %(tc, result))