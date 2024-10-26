'''
뿔이 한 개 달린 유니콘과 뿔이 두 개 달린 트윈혼이 있다.
n개의 뿔과 m 마리의 짐승이 있을 때, 유니콘의 수와 트윈혼의 수는 몇 마리일까?
'''
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 방정식으로부터 유니콘과 트윈혼의 수 계산
    twin_horn = N - M
    unicorn = M - twin_horn
    print(f"#{test_case} {unicorn} {twin_horn}")