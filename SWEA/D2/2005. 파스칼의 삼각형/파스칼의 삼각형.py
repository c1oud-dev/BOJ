'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합의 구성됨
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case}")
    print(1)
    for i in range(1, N):
        pascal = [0]
        pascal[0] = 1
        for j in range(i - 1):
            pascal.append(i)
        pascal.append(1)
        print(*pascal)