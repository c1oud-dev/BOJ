'''
1주일에 L분 이상 U분 이하의 운동을 해야 함
이번 주에 X분만큼 운동을 했다.
제한되어 있는 시간을 넘은 운동을 한 것인지, 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는 출력
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    l, u, x = map(int, input().split())
    result = 0
    if u < x: #초과 운동
        result = -1
    elif x < l: #필요한 운동량
        result = l - x
    else:
        result = 0
    print("#%d %d" %(tc, result))