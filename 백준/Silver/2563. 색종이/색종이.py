N = int(input())  # 색종이 수
paper = [[0] * 100 for _ in range(100)]  # 100x100 크기의 도화지 배열 생성

for _ in range(N):
    x, y = map(int, input().split())
    # 색종이가 차지하는 영역을 1로 표시
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 검은 영역 넓이 계산
black_area = sum(sum(row) for row in paper)
print(black_area)