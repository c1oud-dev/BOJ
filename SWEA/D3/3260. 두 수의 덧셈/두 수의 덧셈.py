T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"#{test_case} {A+B}")
