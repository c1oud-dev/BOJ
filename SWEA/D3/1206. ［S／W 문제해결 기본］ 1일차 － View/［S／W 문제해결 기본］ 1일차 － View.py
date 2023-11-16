'''
19:45 - 20:27
왼쪽과 오른쪽으로 창문을 열였을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다.
조망권이 확보된 세대의 수를 반환해야 한다.

첫 번째부터 이전 2번째까지와 이후 2번째까지 비교를 한다. 리스트 4개 중에서 max값을 찾고 현재 아파트와의 차이를 저장
'''
for tc in range(1, 11):
    n = int(input())
    apart = list(map(int, input().split()))
    ans = 0
    for i in range(4, n):
        if apart[i-3] >= apart[i-2] or apart[i-1] >= apart[i-2]: #일단 바로 앞의 아파트부터 판별
            continue
        else:
            if apart[i-4] >= apart[i-2] or apart[i] >= apart[i-2]:
                continue
            else:
                max_apart = max(apart[i-4], apart[i-3], apart[i-1], apart[i])
                ans += (apart[i-2] - max_apart)
    print('#'+str(tc), ans)