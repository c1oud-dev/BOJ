from collections import deque

#입력
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)] #입력
date = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([])

#토마토가 있는 위치만 큐에 넣기
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if -1 < nx < n and -1 < ny < m and tomato[nx][ny] == 0:
                #익히고 1을 더해주면서 횟수를 세어준다.
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])

bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    date = max(date, max(i))
#결과
print(date - 1)