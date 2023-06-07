import sys
input = sys.stdin.readline
from collections import deque

#좌부터
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def bfs(x, y):
    #[x][y] = 1 #방문표시
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for z in range(8):
            nx = dx[z] + x
            ny = dy[z] + y

            if  0 <= nx < M and 0 <= ny < N: #수정
                if graph[nx][ny] == 1:
                    #visited[nx][ny] == 1 #방문표시
                    graph[nx][ny] = 0
                    q.append((nx, ny))

M, N = map(int, input().split()) #행, 열
graph = [list(map(int, input().split())) for _ in range(M)]
cnt = 0 #글자 수

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)