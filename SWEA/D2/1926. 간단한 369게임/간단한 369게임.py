'''
369 게임이다. 3,6,9가 한 번 들어가면 -를 출력하고 박수를 두 번쳐야 할 때는 --을 출력한다.

풀이 : 단순 구현
두 자리 수 이상부터는 숫자를 분리해서 판단해야 한다. = map 사용
'''
#19:10 - 19:40
from collections import Counter
n = int(input())
num = []
for i in range(1, n+1):
    '''if i < 10: #i가 한 자리 수 일 때
        if i == 3 or i == 6 or i == 9:
            print('-', end = " ")
        else:
            print(i, end = " ")
    else: #두자리 이상일 때'''
    num = list(map(int, str(i)))  #정수 분리, 리스트로 감싸줘야 함 안 그러면 map object 나옴
    if 3 in num or 6 in num or 9 in num: #13일 때
        #개수만큼 출력
        cnt = 0
        count_num = Counter(num)
        for key, value in count_num.items():
            if key == 3 or key == 6 or key == 9:
                cnt += value #개수 저장
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ") #369 아닌 건 출력