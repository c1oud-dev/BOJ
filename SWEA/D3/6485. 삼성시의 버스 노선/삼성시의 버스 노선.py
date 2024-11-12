T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())
    bus = [0]*5000
    for _ in range(N):
        A, B = map(int, input().split())
        for j in range(A - 1, B):
            bus[j] += 1
    P = int(input())
    result = []
    for _ in range(P):
        stop = int(input())
        result.append(bus[stop - 1])
    print(f"#{test_case}", *result)