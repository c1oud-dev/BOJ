'''
모든 양의 유리수를 정확히 하나씩 포함하고 있는 트리
트리의 루트는 1/1, 각 노드는 왼쪽 자식 a/a+b, 오른쪽 자식 a+b/b를 나타냄
루트 노드에서부터 자식을 따라 내려간 방향이 순서대로 주어질 때, 마지막에 위치한 노드가 유리수를 나타내는지 구한다.
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    node = input().strip()
    l = 1
    r = 1
    for i in node:
        if i == 'L':
            r += l
        else:
            l += r
    print("#%d %d %d" %(tc, l, r))
