def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        budget -= i
        if budget < 0:
            budget += i
            break
        else:
            answer += 1
    return answer