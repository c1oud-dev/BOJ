'''
13:35 - 13:39
하나는 A원, 다른 하나는 B원의 빵이 있다.
현재 C원이 있을 때 어떤 빵이든 상관 없이 많은 개수의 빵을 살 수 있다.
두 종류의 개수를 다르게 혹은 한 종류의 빵만 사도 된다.
최대 몇 개의 빵을 살 수 있는가?
'''
t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    if c // a > c // b:
        print('#'+str(tc), c//a)
    else:
        print('#'+str(tc), c//b)