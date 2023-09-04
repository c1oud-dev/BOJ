import sys
input = sys.stdin.readline

N = int(input())
n = []
sorted_n = []
for _ in range(N):
    w, l = map(int, input().split()) #마지막 것만 리스트에 저장됨
    n.append((w, l)) #따라서 append 해줘야 함

for i in n:
    rank = 1
    for j in n:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")