'''
#13:20 - 13:26
각 과목의 점수는 정수, 만점은 100점이다.
성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다. 성적표에 나타나는 총점이 가장 크도록 성적표를 만들고 싶다.
최대로 만들 수 있는 총점은 몇점인지 구해라
'''
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    ans = 0
    score.sort(reverse=True)
    for i in range(k):
        ans += score[i]
    print('#'+str(tc), ans)