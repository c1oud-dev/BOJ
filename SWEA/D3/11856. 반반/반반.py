'''
길이 4의 알파벳 대문자로 이루어진 문자열이 주어졌을 때,
정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 두 번 등장하는지 판별하라.
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    s = input().strip()
    s_set = set(s)
    if len(s_set) == 2:
        result = "Yes"
    else:
        result = "No"
    print("#%d %s" % (tc, result))