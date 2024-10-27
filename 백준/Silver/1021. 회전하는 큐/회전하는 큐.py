'''
N 개의 원소를 포함하고 있는데 양방향 순환 큐를 가지고 있다. 이 큐에서 몇 개의 원소를 뽑아 내려고 한다.
다음 3가지 연산 가능
1. 첫 번째 원소를 뽑아낸다.
2. 왼쪽으로 한 칸 이동시킨다. a2, ..., ak, a1
3. 오른쪽으로 한 칸 이동시킨다. ak, a1, ..., ak-1
뽑아내려고 하는 원소의 위치가 주어짐
순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값
'''
from collections import deque

n, m = map(int, input().split())
pop_num = list(map(int, input().split()))
n_deq = deque()
for i in range(1, n + 1):
    n_deq.append(i)
result = 0
for i in pop_num:
    while i in n_deq:
        if n_deq.index(i) == 0:  # 0번 인덱스가 빼내려는 수랑 같을 때까지
            n_deq.popleft()
        elif n_deq.index(i) <= len(n_deq) // 2:  # 중간보다 이하일 때 왼쪽으로
            n_deq.rotate(-1)  # 1만큼 왼쪽으로 회전(반시계)
            result += 1
        else:
            n_deq.rotate(1)  # 1만큼 오른쪽으로 회전(시계)
            result += 1
print(result)