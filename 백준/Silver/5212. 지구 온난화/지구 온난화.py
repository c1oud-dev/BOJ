R, C = map(int, input().split())
maps = [input().strip() for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
future_map = [["."]*C for _ in range(R)]

for x in range(R):
    for y in range(C):
        sea = 0
        if maps[x][y] == "X":  # 땅이면 주위가 바다인지 탐색
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or nx >= R or ny < 0 or ny >= C:  # 범위를 벗어나면
                    sea += 1
                elif maps[nx][ny] == ".":  # 인접한 곳이 바다이면
                    sea += 1  # 바다 개수 카운트
            if sea < 3:  # 인접한 바다가 세 칸 미만이면
                future_map[x][y] = "X"  # 땅으로 바꾸기

# 땅 영역의 최소, 최대 행과 열 찾기
min_row, max_row = R, 0
min_col, max_col = C, 0

for x in range(R):
    for y in range(C):
        if future_map[x][y] == "X":
            min_row = min(min_row, x)
            max_row = max(max_row, x)
            min_col = min(min_col, y)
            max_col = max(max_col, y)

# 최소, 최대 범위에 맞게 출력
for x in range(min_row, max_row + 1):
    print("".join(future_map[x][min_col:max_col + 1]))