'''
푸른 자성체는 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체는 S극에 이끌리는 성질이 있다.
자성체들이 서로 충돌하여 테이블 위해 남아있는 교착 상태의 개수를 구하라
1은 n극, 2는 s극 성질을 갖는 자성체를 의미

한 줄 씩 확인, 1+2로 된 것만 찾기
'''

for tc in range(1, 11):
    length = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for i in range(100):
        bit = 1
        for j in range(100):
            if table[j][i] == 1:
                bit = 2
            elif table[j][i] == bit:
                bit = 1
                result += 1
    print("#%d %s" % (tc, result))