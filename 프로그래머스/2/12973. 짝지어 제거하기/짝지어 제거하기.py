def solution(s):
    stack = []
    for i in s:
        if not stack:  # 스택이 비어있으면
            stack.append(i)
            continue

        if stack[-1] == i:  # 스택 맨 뒤 요소와 같으면
            stack.pop()
            continue
            
        stack.append(i)  # 위 조건이 모두 맞지 않으면
    return 0 if stack else 1