'''
삼각형 세 변의 길이가 주어질 때
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
주어진 조건을 모두 만족하지 못하는 경우 "Invalid"를 출력(가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면)
'''
#13:45 - 14:45 이후에 풀이 봄..

import sys
input = sys.stdin.readline

while True:
    num = sorted(list(map(int, input().split())), reverse=True)
    if num[0] == 0 and num[1] == 0 and num[2] == 0:
        break
    if num[0] >= num[1] + num[2]: #등호 안 붙여줘서 계속 오류
            print('Invalid')
    elif num[0] == num[1] == num[2]:
        print('Equilateral')
    elif num[0] == num[1] or num[1] == num[2] or num[2] == num[0]: #반례 1 1 2 답 : Invalid -> 이 줄이 제일 문제였던 듯
        print('Isosceles')
    else:
        print('Scalene')