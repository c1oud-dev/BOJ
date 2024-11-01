from collections import Counter

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    word = input().strip()
    char_count = Counter(word)

    result = []
    for char, count in char_count.items():
        if count % 2 != 0:
            result.append(char)
    result = ''.join(sorted(result))

    if not result:
        result = "Good"

    print(f"#{test_case} {result}")