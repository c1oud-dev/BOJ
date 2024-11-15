'''
양의 정수 n을 이진수로 표현한 후 1의 위치 찾기(오름차순)
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    n = format(int(input()), 'b')[::-1] # 양의 정수 n -> 이진수 변환 -> 뒤집기
    result = []
    for i in range(len(n)):
        if n[i] == '1':
            result.append(i)
    print(*result)