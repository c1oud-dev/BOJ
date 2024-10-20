'''
bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것
예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
원래 상태가 주어질 때 초기화 상태(모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    memory = list(map(int, input()))
    result = 0
    bit = 0
    for i in memory:
        if bit != i:
            bit = i
            result += 1

    print("#%d %s" % (tc, result))