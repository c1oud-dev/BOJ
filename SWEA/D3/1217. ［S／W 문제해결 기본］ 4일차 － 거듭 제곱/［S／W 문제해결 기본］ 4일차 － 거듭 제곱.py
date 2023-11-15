def calc(n, m):
    if m == 0:
        return 1
    else:
        ans = n*calc(n, m-1)
    return ans

for _ in range(10):
    cnt = 0
    case = int(input())
    n, m = map(int, input().split())
    print('#'+str(case), calc(n, m))