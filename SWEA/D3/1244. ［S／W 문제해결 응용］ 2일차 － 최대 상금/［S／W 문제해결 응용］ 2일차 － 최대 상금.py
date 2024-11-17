from collections import deque

def bfs(cards, k):
    queue = deque([(cards, 0)])  # 초기 상태: (숫자 리스트, 교환 횟수)
    visited = set()  # 방문한 상태를 저장하기 위한 집합
    max_reward = 0

    while queue:
        current, depth = queue.popleft()
        if depth == k:  # 교환 횟수를 다 사용한 경우
            max_reward = max(max_reward, int(''.join(current)))
            continue

        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                # 숫자 교환
                current[i], current[j] = current[j], current[i]
                next_state = ''.join(current)

                # 방문하지 않은 상태라면 큐에 추가
                if (next_state, depth + 1) not in visited:
                    visited.add((next_state, depth + 1))
                    queue.append((list(next_state), depth + 1))

                # 원상복구
                current[i], current[j] = current[j], current[i]

    return max_reward

# 입력 처리 및 실행
T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    number, k = input().split()
    cards = list(number)
    k = int(k)

    result = bfs(cards, k)
    print(f"#{test_case} {result}")
