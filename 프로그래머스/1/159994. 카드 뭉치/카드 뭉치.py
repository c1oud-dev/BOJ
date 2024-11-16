from collections import deque

def solution(cards1, cards2, goal):
    answer = "Yes"
    cards1 = deque(cards1)  # 큐 생성
    cards2 = deque(cards2)

    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.popleft()
        elif cards2 and i == cards2[0]:
            cards2.popleft()
        else:
            answer = "No"
            break

    return answer