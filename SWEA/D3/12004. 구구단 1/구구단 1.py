'''
N 이 1 이상 9 이하의 두 수 a, b의 곱으로 표현될 수 있는지 판단
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())

    result = "No"
    for i in range(1, 10):  # 1 이상 9 이하
        if N % i == 0 and N // i < 10:  # i 가 N의 약수이면서 10 이하
            result = "Yes"

    print(f"#{test_case} {result}")