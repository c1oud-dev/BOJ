'''
정수 N이 주어질 때, 모든 변의 길이가 N인 가장 넓은 평행사변형 넓이를 출력
평행사변형 넓이 = 밑변 * 높이
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    print("#%d %d" % (tc, n * n))