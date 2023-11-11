'''
23:10 - 23:14
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구한다.

풀이
2로 나눠지는 것과 그렇지 않은 것을 나눔
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    ans = 1 #1에서 시작하므로
    for i in range(2, n+1): #2부터 계산
        if i % 2 == 0: #짝수인 건 마이너스
            ans -= i
        else: #홀수인 건 플러스
            ans += i
    print('#'+str(tc), ans)
#1차 제출 실패 - tc를 i라고 적어서 런타임 에러