'''
24시간제
자정에서부터 정확히 A시간이 지났다. B시간이 더 지나면 몇 시일까?
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    result = 0
    result = a + b
    if result >= 24: #24시간 이상이면
        result -= 24
    print("#%d %d" %(tc, result))