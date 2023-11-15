'''
06:18 - 06:20
양의 정수가 주어질 때, 이 수가 홀수인지 짝수인지 판별한다.
홀수이면 Odd, 짝수이면 Even 출력
'''

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    if n % 2 == 0:
        print('#'+str(tc), 'Even')
    else:
        print('#' + str(tc), 'Odd')