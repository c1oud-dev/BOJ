from collections import deque
m, n = map(int, input().split())
a=[]
q=list(map(int,input().split()))
for i in range(1,m+1):
    a.append(i)
a=deque(a)
cnt=0
for x in q:
    idx=0
    m=0
    if a[0]==x:
        a.popleft()
    else:
        for j in range(len(a)):
            if a[j]==x:
                idx=j
        if idx<=len(a)//2:
            m=idx
            cnt+=m
            while m!=0:
                a.append(a.popleft())
                m-=1
            a.popleft()
        else:
            m=len(a)-idx
            cnt+=m
            while m!=0:
                a.appendleft(a.pop())
                m -= 1
            a.popleft()
print(cnt)