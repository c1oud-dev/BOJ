'''
00:15 - 00:17
10개의 수의 평균값을 소수점 첫째 자리에서 반올림한 정수를 출력
풀이
sum(), round() 사용
'''
t = int(input())
for tc in range(1, t+1):
    num = list(map(int, input().split()))
    print('#'+str(tc), round((sum(num) / 10)))