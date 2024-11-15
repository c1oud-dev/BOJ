result, max_on = 0, 0
for _ in range(10):
    off, on = map(int, input().split())
    max_on -= off
    max_on += on
    result = max(result, max_on)
print(result)