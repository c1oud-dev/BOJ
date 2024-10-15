'''
A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소 공배수라고 한다.
A와 B의 최소공배수를 구하라
'''
import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = abs(a * b) // math.gcd(a, b)
    print(result)