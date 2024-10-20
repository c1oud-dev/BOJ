'''
몇 개의 조로 나누려고 한다.
한 조가 2명 이하의 학생으로 구성되면 안됨
3명 이상의 학생으로 구성된 조의 수를 최대화하려고 함
3명 이상의 학생으로 구성된 조의 수의 최댓값이 얼마인지를 구하라
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input()) #학생 수
    result = 0
    #n을 3으로 나누면 됨
    print("#%d %d" %(tc, int(n / 3)))