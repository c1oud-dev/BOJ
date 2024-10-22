'''
직사각형의 나머지 한 변의 길이를 구하라
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    square = list(map(int, input().split()))
    result = 0
    if square[0] == square[1]:
        result = square[2]
    elif square[1] == square[2]:
        result = square[0]
    else:
        result = square[1]
    print("#%d %s" % (tc, result))