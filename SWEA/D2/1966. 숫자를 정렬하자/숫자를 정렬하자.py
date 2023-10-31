#20:40 - 20:50

t = int(input())
for i in range(1, t+1):
    ans = 0
    n = int(input()) #for문에 안 넣어줘서 틀림
    num = list(map(int, input().split()))
    ans = sorted(num)
    print("#"+str(i),*ans)
    num = []