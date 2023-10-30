p, k = map(int, input().split())
#p > k
if p > k:
    print(p - k + 1)
else:
    print(k - p + 1)