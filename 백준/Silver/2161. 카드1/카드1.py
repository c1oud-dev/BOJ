'''
제일 위에 있는 카드를 바닥에 버린다.
그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드 출력
'''
from collections import deque

n = int(input())
card_deq = deque(range(1, n + 1))  # n 만큼 큐에 넣기
result = []
while card_deq:
    result.append(card_deq.popleft())
    card_deq.rotate(-1)
print(*result)