'''
00:25 - 00:27
2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력
풀이
단순 구현, 비교연산자 사용
'''
t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    if a < b:
        print('#' + str(tc), '<')
    elif a > b:
        print('#' + str(tc), '>')
    else:
        print('#' + str(tc), '=')