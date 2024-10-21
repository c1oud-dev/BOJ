'''
40점 미만인 학생은 보충학습을 받고 점수를 40점으로 올릴 수 있다.
최대 40점 받을 수 있는데, 보충 학습을 받은 후 점수 평균을 구하라
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    score = list(map(int, input().split()))
    result = 0
    for i in score:
        if i < 40:
            result += 40
        else:
            result += i
    result = int(result / 5)
    print("#%d %s" % (tc, result))
