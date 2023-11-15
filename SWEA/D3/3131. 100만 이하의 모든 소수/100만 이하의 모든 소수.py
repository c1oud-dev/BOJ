'''
08:22 - 08:31
1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

에라토스테네스의 체
'''
n = 10**6
a = [True]*(n+1)
m = int(n**0.5)

for i in range(2, m+1):
    if a[i] == True:
        for j in range(i+i, n+1, i):
            a[j] = False
print(*[i for i in range(2, n+1) if a[i] == True])