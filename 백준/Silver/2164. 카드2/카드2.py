'''
한 장 남을 때까지 다음과 같은 동작을 반복한다.
1. 제일 위에 있는 카드를 바닥에 버린다.
2. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
위 과정을 반복하고 마지막에 남게 되는 카드를 구한다.
'''
#18:10 - 18:20

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque() #덱 생성
for i in range(1, n+1):
    q.append(i)

while len(q) > 1:
    q.popleft() #윗 장 버리기
    q.append(q[0]) #밑으로 옮기기
    q.popleft()
print(q[0])

#pop은 맨 뒤에서부터 빠짐