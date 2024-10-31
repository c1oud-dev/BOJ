'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산
'''

for test_case in range(1, 11):
    _ = int(input())
    infix = input()  # 중위 표기식
    stack = []
    postfix = []
    result = 0
    for i in infix:
        if i == "+":
            stack.append(i)
        else:
            postfix.append(i)
            if len(stack) > 0:
                postfix.append(stack.pop(0))
    for i in postfix:
        if i != "+":
            result += int(i)
    print(f"#{test_case} {result}")