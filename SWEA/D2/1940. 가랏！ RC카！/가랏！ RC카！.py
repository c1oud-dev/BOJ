'''
0 : 현재 속도 유지.
1 : 가속
2 : 감속
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    command = int(input())  # 커맨드 수
    result = 0
    now = 0 # 현재 속도
    for _ in range(command):
        com = list(map(int, input().split()))
        if len(com) == 2:  # 명령어가 1 or 2 일 때
            if com[0] == 1:  # 1일 때
                now += com[1]
            else:  # 2일 때
                if now < com[1]:  # 현재 속도보다 감속할 속도가 더 클 경우
                    now = 0
                else:
                    now -= com[1]
        result += now

    print(f"#{test_case} {result}")