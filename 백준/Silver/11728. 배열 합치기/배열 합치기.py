'''
정렬되어있는 두 배열 A, B를 합친 후 정렬해서 출력한다.
첫째 줄에는 배열 A, B의 크기 N과 M이 주어진다. (1부터)
둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다.

풀이 - 정렬, 투포인터
'''
#19:40 - 20:00
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
#정렬
'''num = []
for _ in range(2):
    num += input().split() #['3', '5', '2', '9']
ans = []
for i in num:
    ans.append(int(i))
ans.sort() #문자형이라도 정렬이 된다. 그러나 사전순으로 정렬 됨 즉, 100과 11일 때 출력이 100 11임. 정답은 11 100
print(*ans)
#1차 제출 실패 - 문자형이므로 사전순으로 정렬됨. 그래서 정수형 변환 코드 추가'''

#투 포인터
a = list(map(int, input().rsplit())) #rsplit() : 오른쪽부터 문자열을 지정 구분자(기본값 : 공백) 기준으로 잘라서 리스트 생성
b = list(map(int, input().rsplit()))

left, right = 0, 0
ans = []
while left < n and right < m:
    if a[left] < b[right]:
        ans.append(a[left]) #3
        left += 1
    else:
        ans.append(b[right])
        right += 1

while left < n:
    ans.append(a[left])
    left += 1

while right < m:
    ans.append(b[right])
    right += 1

print(' '.join(map(str, ans)))