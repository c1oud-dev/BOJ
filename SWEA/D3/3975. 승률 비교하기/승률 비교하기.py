T = int(input())  # 테스트 케이스 수
results = []  # 결과를 저장할 리스트

for test_case in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    alice = A * D  # 분수 비교를 위해 곱셈
    bob = C * B

    if alice> bob:
        results.append(f"#{test_case} ALICE")
    elif alice < bob:
        results.append(f"#{test_case} BOB")
    else:
        results.append(f"#{test_case} DRAW")

# 저장한 결과를 한 번에 출력
print("\n".join(results))