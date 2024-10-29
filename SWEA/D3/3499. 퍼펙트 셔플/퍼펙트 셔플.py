'''
카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고
나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 말함
N 개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플한 순서 출력
홀수이면 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 된다.
'''
from collections import deque
import math

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())  # 카드 수
    card = input().split()

    # 절반으로 나눈 덱을 deque로 만들어 popleft()로 효율적인 제거 수행
    first_half = deque(card[:math.ceil(N / 2)])
    second_half = deque(card[math.ceil(N / 2):])

    result = []
    # 두 반쪽을 교차로 섞어 새로운 덱을 생성
    while second_half:
        result.append(first_half.popleft())
        result.append(second_half.popleft())

    # 홀수일 때 첫 번째 반쪽에 한 장 더 남아있는 경우 추가
    if first_half:
        result.append(first_half.popleft())

    # 결과 출력
    print(f"#{test_case} {' '.join(result)}")