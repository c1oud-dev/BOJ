'''
최빈수(가장 많이 나타나는 값)를 이용해 학생들의 평균 수준을 짐작할 수 있다.
점수 중 최빈수를 출력해야 하는 문제이다. 다만, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력해야 한다.
학생의 수는 1000명이고, 학생의 점수는 0점~100점 값이다.
테스트 케이스가 주어지고, 각 테스트 케이스의 첫 줄에는 케이스의 번호가 주어지고, 그 다음줄부터는 점수가 주어진다.

풀이
총 1000명을 탐색해야 한다. collections 모듈의 Counter 함수를 사용한다.
counter 함수는 같은 값끼리 묶고 그 개수를 센다.
counter한 후 max 내장함수를 사용해 최댓값을 출력한다.
'''
#16:57 - 17:08(1차 제출) - 17:38(2차 제출) - 17:41(3차 제출)
from collections import Counter
t = int(input())
for _ in range(t):
    test_number = int(input())
    ans = 0
    count_score = []
    score = list(map(int, input().split()))
    # max를 쓰면 key의 최댓값을 반환함. 그래서 values함수 사용
    count_score = Counter(score) #.most_common() #most_common() : 빈도수가 많은 요소 순대로 정렬
    #count_score = sorted(count_score, key=lambda x:x[0]) #value 기준으로 내림차순 정렬하려고 했는데 안 됨
    #print(sorted(count_score, key=count_score.get, reverse=True)) #이렇게 하면 key만 출력되고, value의 최댓값이 반환이 되지 않음
    count_score = sorted(count_score.items(), key=lambda pair: pair[1], reverse=True)#이렇게 하면 key 기준으로 내림차순 정렬
    ans = count_score[0][0]
    print("#"+str(test_number), ans)
#1차 제출 실패 - 이유는 print에 테스트 케이스 번호도 출력해야 하는데 안 넣었음
#그리고 values를 사용하면 키값을 출력하지 못함, 정렬한 후에 첫 번째 key값 출력