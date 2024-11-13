def dfs(index, score, cal):
    global max_score

    if cal > L:
        return
    if index == N:
        max_score = max(max_score, score)
        return
    dfs(index + 1, score + ingredients[index][0], cal + ingredients[index][1])

    dfs(index + 1, score, cal)

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]

    max_score = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {max_score}")