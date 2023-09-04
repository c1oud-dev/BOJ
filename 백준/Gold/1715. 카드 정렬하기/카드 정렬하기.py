import sys
input = sys.stdin.readline

from queue import PriorityQueue #우선순위 큐 클래스(queue = 내장 모듈)
#우선순위 큐는 제거될 때 가장 작은 값을 제거한다. 정렬할 필요가 없겠죠?

n = int(input())
card = [] #카드 묶음을 담을 리스트
for _ in range(n):
    card.append(int(input())) #card[10, 20, 30]

#작은 것부터 묶어서 비교하는 것이 효율적
#card.sort() #오름차순 정렬 / reversed = True : 내림차순 정렬

q = PriorityQueue() #우선순위 큐 생성
#큐가 빌 때까지 반복
#1. 큐에 카드묶음을 모두 넣기
for i in card:
    q.put(i)
#2. 작은 묶음 두 개를 비교
res = 0 #출력할 결과
while q.qsize() > 1:
    x = q.get() #큐에서 가장 작은 값을 제거하고 x에 저장
    sum = x + q.get()
    res += sum
    q.put(sum)
print(res)