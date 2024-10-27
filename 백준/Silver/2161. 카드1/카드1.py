from collections import deque
n=int(input())
card=[]
trash=[]
for x in range(1,n+1):
    card.append(x)
card=deque(card)
while card:
    trash.append(card.popleft())
    if len(card) != 0:
        card.append(card.popleft())
print(*trash)