import sys
input = sys.stdin.readline

N,K = map(int, input().split())
m = int(N**0.5) #제곱근
a = [True]*(N+1) #소수 판정하기 위함

cnt = 0
for i in range(2, N+1):
    if a[i] == True: #소수이면
        a[i] = False #소수도 지우고
        cnt += 1
        if cnt == K:
            print(i)
        for j in range(i + i, N + 1, i): #배수도 지우기
            if a[j] == True: #지워지지 않은 것만 
                a[j] = False
                cnt += 1
                if cnt == K:
                    print(j)