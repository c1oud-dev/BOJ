'''
가장 높은 층으로 가고자 함
가만히 놔둘지, 아니면 위로 i층을 올릴지 정할 수 있다.
P층에 도착하지 않도록 모든 순간에 적절히 선택을 해야 한다.
모든 N번의 선택이 끝났을 때 당신이 있을 수 있는 가장 높은 층의 번호를 구하라.
'''
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N, P = map(int, input().split())
    result = 0
    for i in range(1, N + 1):
        result += i
        if result == P:
            result -= 1

    print(result)