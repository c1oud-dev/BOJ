'''
'a'에서 'z'까지 총 26가지 문자가 있다.
앞에서부터 몇 개의 알파벳이 순서에 맞게 적혀 있는지 구하라.
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    input_alpha = input().strip()
    alpha = "abcdefghijklmnopqrstuvwxyz"  # 알파벳
    result = 0

    while result < len(input_alpha):
        if input_alpha[result] == alpha[result]:
            result += 1
        else:
            break
    print(f"#{test_case} {result}")