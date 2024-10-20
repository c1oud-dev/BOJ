'''
팰린드롬 수 : 앞 뒤가 똑같은 문자열
양의 정수 N에 대해서, N과 루트 N이 모두 팰린드롬이면 이 수를 제곱 팰린드롬 수라고 한다.
A이상 B이하 제곱 팰린드롭 수는 몇 개인가?
'''
import math
test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    result = 0

    for i in range(a, b + 1):
        reversed_num = int(str(i)[::-1]) #정수 뒤집기
        sqrt_num = math.sqrt(i)  #제곱근, sqrt는 float형으로 반환
        #소수점 뒤가 0이면 버리기
        sqrt_num = "{:g}".format(sqrt_num) # <class 'str'>
        #print(type(sqrt_num)) 타입 확인 방법
        reversed_sqrt_num = str(sqrt_num)[::-1] #제곱근 뒤집기

        if i == reversed_num and sqrt_num == reversed_sqrt_num:
            result += 1

    print("#%d %s" % (tc, result))

'''
reverse()는 문자열만 가능
따라서 정수는 슬라이싱 이용 혹은 정수를 문자로 변환 후 reverse 사용
int(str(num)[::-1])
'''