'''
문자열에서 모음만 사라진 문자열을 출력
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    word = input().strip()
    vowel = ["a", "e", "i", "o", "u"]
    result = " "
    for i in word: #문자열도 for문에서 하나씩 꺼내기 가능
        if i not in vowel:
            result += i

    print("#%d%s" %(tc, result))