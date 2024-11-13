T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    card = input().strip()
    S, D, H, C = [0]*13, [0]*13, [0]*13, [0]*13
    for i in range(0, len(card), 3):
        shape = card[i]  # 카드 종류
        num = int(card[i + 1:i + 3])  # 카드 수
        if shape == 'S':
            S[num - 1] += 1
        elif shape == 'D':
            D[num - 1] += 1
        elif shape == 'H':
            H[num - 1] += 1
        elif shape == 'C':
            C[num - 1] += 1

    result = [S, D, H, C]
    error = ""
    for i in result:
        for j in i:
            if j > 1:
                error = "ERROR"
                break

    result = [S.count(0), D.count(0), H.count(0), C.count(0)]
    if error == "":
        print(f"#{test_case}", *result)
    else:
        print(f"#{test_case} {error}")
