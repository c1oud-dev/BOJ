import sys
input = sys.stdin.readline

n = int(input())
#dp 함수, bottom-up
dp = [0]*(n+1)
dp[1] = 1
def fibo(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fibo(n))