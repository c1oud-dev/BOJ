def solution(s):
    from collections import deque
    answer = True
    queue = deque()  # 비어있는 큐 생성
    for i in s:
        if i == "(":
            queue.append(i)  # 뒤에서부터 넣기
        else:
            if len(queue) != 0:  # 큐가 비어있지 않으면
                queue.pop()  # 맨 뒤에서부터 꺼내기
            else:  # 큐가 비어있으면
                queue.append(i)
                break

    if len(queue) > 0:  # 큐가 비어있지 않으면 올바르게 짝지어있지 않았다는 것
        answer = False

    return answer