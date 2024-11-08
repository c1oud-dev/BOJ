'''
각 상자에 들어 있는 사탕의 개수가 순증가하기를 원한다.
즉, 두 번째 상자에 들어 있는 사탕의 개수가 첫 번째 상자에 들어 있는 사탕의 개수보다 더 많아야 하고,
세 번째 상자도 마찬가지.
또한 모든 상자가 비어 있으면 안 됨
이 두 조건을 만족하기 위해, 상자 속에 들어있는 사탕을 먹어 없애 버리는 것
세현이가 조건을 만족시킬 수 있는지 판단하고, 만족시킬 수 있다면 최소 몇 개의 사탕을 먹어야 하는지 구하라.

2 번째 인덱스부터 1번째 인덱스 순으로 확인
'''
T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = 0

    while B >= C and B > 1:
        B -= 1
        result += 1
    while A >= B and A > 1:
        A -= 1
        result += 1
    if A == B or A == C:
        result = -1

    print(f"#{test_case} {result}")
