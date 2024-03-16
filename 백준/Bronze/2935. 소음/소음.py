'''
학생들은 덧셈과 곱셈만 배웠다.
또, 아직 10의 제곱꼴을 제외한 다른 수는 학교에서 배우지 않았기 때문에, 선생님이 써주는 수는 모두 10의 제곱 형태이다.
숫자는 최대 100자리이다. 칠판에 쓰여 있는 문제가 주어졌을 때, 결과를 구하는 프로그램을 작성하시오.
'''
#21:04 - 21:07

#import sys
#input = sys.stdin.readline

a = int(input())
str = input()
b = int(input())
if str == "*":
    print(a*b)
else:
    print(a+b)