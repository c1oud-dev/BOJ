T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    word = input().strip()
    word = sorted(word)  # 정렬하기

    result = ""
    for i in word:
        if word.count(i) % 2 != 0:
            if i not in result:
                result += i

    if len(result) == 0:
        result = "Good"

    print(f"#{test_case} {result}")