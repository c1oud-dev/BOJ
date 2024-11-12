T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0]*N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for l in range(L - 1, R):
            box[l] = i

    print(f"#{test_case} {' '.join(map(str, box))}")