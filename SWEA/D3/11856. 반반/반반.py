'''
길이 4의 알파벳 대문자로 이루어진 문자열이 주어졌을 때,
정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 두 번 등장하는지 판별하라.
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    s = input().strip()
    s_sort = sorted(s) #리스트 형태
    result = ""
    if s_sort[0] == s_sort[1] and s_sort[2] == s_sort[3] and s_sort[0] != s_sort[2]:
        result = "Yes"
    else:
        result = "No"

    print("#%d %s" % (tc, result))