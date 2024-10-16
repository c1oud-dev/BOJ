test_case = int(input())
for _ in range(test_case):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        cnt += 1
    print(cnt)
