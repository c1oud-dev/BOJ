digit = int(input())
ans = 0
car = list(map(int, input().split()))
for i in car:
    if i == digit:
        ans += 1
print(ans)