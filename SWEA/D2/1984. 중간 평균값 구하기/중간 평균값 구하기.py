'''
최댓값과 최솟값을 제외한 나머지 평균값을 출력
풀이 : 리스트의 전체 합에서 최소와 최대를 뺀 후 평균값을 계산한다. 내장함수 sum, max, min을 사용
'''
#21:01 - 21:09
import math #반올림 round함수가 내장되어 있는 math
t = int(input())
for i in range(1, t+1):
    ans = 0
    num = list(map(int, input().split()))
    ans = sum(num) - (max(num) + min(num))
    print("#"+str(i),round(ans/8))
#1차 제출 실패 - 반례 생각 못함, 그리고 문제를 잘못 읽음 = 소수점 첫째 자리에서 반올림한 정수를 출력해야 함