def solution(s):
    answer = []
    for i in range(len(s)):
        cnt = 0
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            for j in s[i-1::-1]:
                cnt += 1
                if s[i] == j:
                    break
            answer.append(cnt)
    return answer