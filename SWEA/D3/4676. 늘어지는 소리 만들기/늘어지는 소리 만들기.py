'''
문자열 사이에 하이픈을 넣는다.
0이면 맨 앞에 하이픈을 넣는다. 1이상이면 문자열 뒤에 하이픈을 넣는다.

insert(i, x) 사용
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    word = list(input().strip())  # 문자열
    h = int(input())  # 하이픈 개수
    hyphen = list(map(int, input().split()))  # 하이픈 위치

    # 하이픈 위치를 오른쪽에서 왼쪽 순서로 처리
    for idx in sorted(hyphen, reverse=True):
        word.insert(idx, '-')

    print(f"#{test_case} {''.join(word)}")