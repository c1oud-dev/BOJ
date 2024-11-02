T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    n = input().split()
    m = input().split()
    Q = int(input())
    result = []
    for _ in range(Q):
        q = int(input())
        result.append(n[q % N - 1] + m[q % M - 1])
    print(f"#{test_case} {' '.join(result)}")