import sys
input = sys.stdin.readline

t = int(input()) #테스트 케이스

def DP(n):
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n):
        dp[i] = dp[i - 3] + dp[i - 2]
    return dp[n-1]

for _ in range(t): #테스트 케이스만큼 반복
    n = int(input())
    if n == 1 or n == 2 :
        print(1)
    else:
        print(DP(n))