import sys
input = sys.stdin.readline

def res(n):
    for i in range(2, n + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
            if n % i != 0:
                print(i, cnt)

for _ in range(int(input())):
    n = int(input())
    m = int(n**0.5)
    res(n)