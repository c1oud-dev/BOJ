'''
약수들 중 k 번째로 작은 수를 출력
'''
N, K = map(int, input().split())
divisor = []  # 약수를 담을 리스트
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        divisor.append(i)
        if N // i != i:
            divisor.append(N // i)

if len(divisor) >= K:
    print(sorted(divisor)[K - 1])
else:
    print(0)