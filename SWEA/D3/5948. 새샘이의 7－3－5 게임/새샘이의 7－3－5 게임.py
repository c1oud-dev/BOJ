'''
07:36 - 07:44
서로 다른 7개의 정수 중 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.
이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력한다.
'''
from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    n = list(map(int, input().split()))
    ans = []
    for i in combinations(n, 3): #list로 안 묶어도 됨
        ans.append(sum(i))
    ans = list(set(sorted(ans, reverse=True))) #중복 제거 해야 함 - set 사용
    print('#'+str(tc), ans[4])