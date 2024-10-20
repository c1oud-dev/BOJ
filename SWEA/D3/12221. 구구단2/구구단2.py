'''
1 이상 9 이하의 자연수 두개를 곱셈할 수 있으나 10 이상의 자연수를 곱셈 방법은 모름
A, B가 주어지면 두 정수를 곱셈할 수 있으면 곱을 출력하고 아니면 -1을 출력

두 정수 중 하나라도 10이상의 수가 존재하면 -1 출력
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    result = 0
    if a >= 10 or b >= 10:
        result = -1
    else:
        result = a * b
    print("#%d %d" % (tc, result))