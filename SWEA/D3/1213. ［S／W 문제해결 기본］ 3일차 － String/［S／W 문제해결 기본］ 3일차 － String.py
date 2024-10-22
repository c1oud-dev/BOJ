'''
문장에서 특정한 문자열의 개수를 반환하라

슬라이싱
'''
for tc in range(10):
    tc_num = int(input())
    word = input().strip()
    sentence = input().strip()
    result = 0
    i= 0
    while True:
        if sentence[i:i + len(word)] == word:
            result += 1
        i += 1
        if i == len(sentence) - len(word) + 1:
            break
    print("#%d %s" % (tc_num, result))