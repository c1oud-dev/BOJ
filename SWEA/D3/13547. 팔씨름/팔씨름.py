'''
15번 팔씨름을 하여 8번 이상 이기는 사람이 점심 값을 면제 받는다.
k 번의 팔씨름 진행, 'o'면 승리, 'x'면 패배
앞으로 팔씨름 15번째 경기까지 진행했을 때 면제받을 가능성이 있으면 YES, 없으면 NO

x 가 8번 이상이면 NO
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    game = input().strip()
    lose = 0
    result = ""
    for i in game:
        if i == "x":
            lose += 1
    if lose >= 8:
        result = "NO"
    else:
        result = "YES"
    print(f"#{test_case} {result}")