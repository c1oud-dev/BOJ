'''
08:07 - 08:09
N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택해 그 합이 K가 되는 경우의 수를 구하라.
'''
from itertools import combinations

t = int(input())
for tc in range(1,t+1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n+1):
        for j in combinations(num, i):
            if sum(j) == k:
                cnt += 1
    print('#'+str(tc),cnt)