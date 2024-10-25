'''
Alice와 Bob은 길이 N미터의 통나무를 자르는 게임을 한다.
게임은 Alice가 먼저 시작하며 그 이후 둘이 번갈아가며 턴을 가진다.
각 턴을 맏은 사람은 통나무를 두 조각으로 나누는데, 이때 잘린 통나무가 모두 자연수 미터 길이를 가지도록 잘라야 한다.
더 이상 자를 수 없게 되는 사람이 진다. 누가 이기는가?

1:N 씩 나눔, N이 짝수면 Alice가 승, 홀수면 Bob이 승
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    if N % 2 == 0:
        result = "Alice"
    else:
        result = "Bob"
    print(f"#{test_case} {result}")