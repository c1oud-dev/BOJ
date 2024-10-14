t = int(input()) #테스트 케이스
for _ in range(t):
    f = int(input())
    n = int(input())
    floors = [i for i in range(1, n + 1)] #0층 리스트
    for j in range(f):
        for k in range(1, n):
            floors[k] += floors[k - 1]
    print(floors[-1])