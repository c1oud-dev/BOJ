import sys
input = sys.stdin.readline
#bfs를 위해 deque 임포트
from collections import deque
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
#최대 높이 찾기
max_value = max(map(max, area)) #9가 최대 높이
#오른쪽부터 시계방향으로 탐색
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

#영역 확인을 하기 위한 bfs
def bfs(rain, x, y): #x = 강수량
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if -1 < nx < N and -1 < ny < N:
                if area[nx][ny] > rain and visited[nx][ny] == 0:
                    visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                    q.append((nx, ny))

res = []
for rain in range(max_value):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 표시
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > rain:
                bfs(rain, i, j)
                cnt += 1
    res.append(cnt)
print(max(res))