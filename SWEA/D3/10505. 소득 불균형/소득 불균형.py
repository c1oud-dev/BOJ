'''
n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수 출력
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input()) #사람 수
    income = list(map(int, input().split())) #소득
    ave = sum(income) / n #평균 계산
    result = 0
    for i in income:
        if ave >= i:
            result += 1
    print("#%d %d" % (tc, result))