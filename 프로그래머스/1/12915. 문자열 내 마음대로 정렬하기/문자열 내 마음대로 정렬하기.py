def solution(strings, n):
    answer = []
    #strings.reverse()
    answer = sorted(strings, key=lambda x:(x[n], x))
    return answer