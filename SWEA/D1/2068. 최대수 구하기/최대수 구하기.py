#22:14 - 22:16

t = int(input())
for i in range(1, t+1):
    num = list(map(int, input().split()))
    print("#"+str(i),max(num))