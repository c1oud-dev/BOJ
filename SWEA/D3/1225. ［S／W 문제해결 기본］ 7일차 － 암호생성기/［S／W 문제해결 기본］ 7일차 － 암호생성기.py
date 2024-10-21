'''
n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
1. 8개의 숫자를 입력 받는다.
2. 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 이러한 작업을 한 사이클이라고 함
3. 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램 종료
결과 : 이때 8자리의 숫자 값이 암호가 된다.

풒이 : 자료 구조, 힙 영역
'''
from collections import deque

for tc in range(10):
    tc_num = int(input())
    data = list(map(int, input().split()))
    data_deque = deque(data)  # 큐 생성
    cycle = 1

    while data_deque:
        num = data_deque.popleft() #가장 왼쪽 값을 반환, 오른쪽 끝은 pop()
        num -= cycle

        if num <= 0: #0보다 작아지거나 0일 경우 0으로 저장
            num = 0
            data_deque.append(num)
            break

        data_deque.append(num) #오른쪽 끝에 새로운 값을 추가, 왼쪽 끝은 appendleft()
        cycle += 1
        if cycle > 5:
            cycle = 1


    print("#%d" % tc_num, end=' ')
    for i in data_deque:
        print("%d" %i, end=' ')
    print()