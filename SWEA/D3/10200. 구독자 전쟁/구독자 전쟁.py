'''
p 채널과 t 채널 모두 구독하고 있는 사람들이 최소 몇 명, 최대 몇 명인지 구해라.

최대는 더 작은 수를 출력하고, 최소는 A + B 가 N 이상일 때 A + B - N이고, 이하일 땐 0이다.
'''
T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    if A + B > N:
        sub_max = min(A, B)
        sub_min = A + B - N
    else:
        sub_max = min(A, B)
        sub_min = 0
    print(f"#{test_case} {sub_max} {sub_min}")