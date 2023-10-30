#22:40 - 23:11
'''
문제 : 회원들의 나이 순대로 정렬(오름차순), 나이가 같을 경우 가입한 순으로 정렬(내림차순)
풀이 : sort() 사용
'''

import sys
input = sys.stdin.readline

n = int(input())
member = []
for _ in range(n):
    age, name = map(str, input().split())
    member.append((int(age), name)) #[(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]

#먼저 나이순으로 정렬
#member.sort() #sort는 디폴트가 오름차순
#첫 번째 인자를 기준으로 먼저 오름차순 정렬, 두 번째 인자를 기준으로 내림차순 정렬
#member.sort(key=lambda x:(x[0], x[1])) #-는 현재정렬차순과 반대로
member.sort(key=lambda x:x[0])
#print(member) #출력할 때 리스트에서 빼내야 함. 그래서 처음 제출했을 때 틀림
for i in member:
    print(*i)