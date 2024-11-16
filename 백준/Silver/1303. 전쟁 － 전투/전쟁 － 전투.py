'''
흰색 옷 위력과 파란색 옷 위력의 합 출력
상하좌우로 인접한 병사들 찾기
'''
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
war = [input().strip() for _ in range(M)]
visited = [[0] * N for _ in range(M)]
W, B = 0, 0

def dfs(i, j, color):
    cnt = 1
    visited[i][j] = 1
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] == 0 and war[nx][ny] == color:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append([nx, ny])
    return cnt

for i in range(M):  # 세로
    for j in range(N):  # 가로
        if war[i][j] == "W" and visited[i][j] == 0:
            W += dfs(i, j, "W") ** 2
        elif war[i][j] == "B" and visited[i][j] == 0:
            B += dfs(i, j, "B") ** 2

print(W, B)