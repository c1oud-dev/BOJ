T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())  # 전선 개수
    a, b = [], []
    for _ in range(N):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)

    result = 0
    for x, y in zip(a, b):
        for i, j in zip(a, b):
            if x < i and j < y:
                result += 1
    print(f"#{test_case} {result}")