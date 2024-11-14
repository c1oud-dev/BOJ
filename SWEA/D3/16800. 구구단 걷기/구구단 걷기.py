'''
곱셈표 위에 서 있다. (i, j) 셀에는 정수 i x j 가 적혀 있다. (구구단 표와 동일)
현재 위치는 (1, 1) 곱셈표의 오른쪽이나 아래쪽 방향으로 이동할 수 있다.
(i, j)에 서 있다면 (i + 1, j)나 (i, j + 1)로 이동 가능
정수 N이 주어졌을 때 N이 적혀 있는 어떤 셀에 도착하기 위해 최소 몇 번 움직여야 하는가?
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())

    # N 약수 구하기
    min_num = N
    x, y = 0, 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if (N // i) - i < min_num:  # 약수의 차가 제일 작은 거
                x = i
                y = N // i
                
    result = (x - 1) + (y - 1)
    print(f"#{test_case} {result}")