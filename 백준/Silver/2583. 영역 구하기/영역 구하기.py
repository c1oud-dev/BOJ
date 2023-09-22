import sys
input = sys.stdin.readline

from collections import deque
sys.setrecursionlimit(10**9) #->런타임 에러 방지/재귀 깊이 변경

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)] #방문 표시

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split()) #입력 받기
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1 #방문 처리
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
#cnt = 1
def DFS(x, y, cnt):
    #global cnt #전역변수
    graph[y][x] = 1 #방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < N and -1 < ny < M and graph[ny][nx] == 0: #사각형이 아닌 곳
                #cnt += 1 #사각형 넓이
                #graph[ny][nx] = 1 #방문 처리
                cnt = DFS(nx, ny, cnt+1)
    return cnt

res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0: #사각형이 아닌 곳만 탐색
            res.append(DFS(j, i, 1))
print(len(res))
print(*sorted(res))