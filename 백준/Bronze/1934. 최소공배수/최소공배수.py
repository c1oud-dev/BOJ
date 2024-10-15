'''
A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소 공배수라고 한다.
A와 B의 최소공배수를 구하라
'''
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = 1
    for i in range(45000, 1, -1): #45000부터 거꾸로 2까지
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
            result *= i
    result *= a * b
    print(int(result))

'''
반례 : 50 50
똑같은 값으로 두 번 나뉘어 질 수 있을 때
'''