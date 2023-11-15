'''
05:12 - 05:17
과제 제출하지 않은 사람 오름차순으로 정렬
'''

t = int(input())
for tc in range(1,t+1):
    n, k = map(int, input().split())
    non = list(map(int, input().split()))
    ans = []
    for i in range(1, n+1):
        if i not in non:
            ans.append(i)
    print('#'+str(tc), *ans)