'''
월급 평균
소수점 이하 여섯 자리까지 출력
계산 방법 += p확률 * x만원
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    result = 0
    for i in range(n):
        p, x = map(float, input().split())
        result += p * x
    result = "{:.6f}".format(result)
    print(f"#{tc} {result}")