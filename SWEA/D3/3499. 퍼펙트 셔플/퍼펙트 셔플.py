'''
카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고
나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 말함
N 개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플한 순서 출력
홀수이면 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 된다.
'''
import math
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())  # 카드 수
    card = list(map(str, input().split()))
    first_half = [card[i] for i in range(math.ceil(N / 2))]  # 카드의 절반에서 앞 카드들만 저장
    second_half = [card[i] for i in range(math.ceil(N / 2), N)]  # 카드의 절반에서 뒤 카드들만 저장
    result = []
    while len(second_half) > 0:
        result.append(first_half.pop(0))  # 첫 번째 원소를 빼서 결과에 넣기
        result.append(second_half.pop(0))
    # 홀수 일때 first 리스트는 하나의 카드가 남기 때문에 따로 추가
    if N % 2 != 0:
        result.append(first_half.pop())
    print(f"#{test_case}", end=' ')
    print(*result)