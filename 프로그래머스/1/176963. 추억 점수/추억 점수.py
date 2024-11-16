def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in name:  # 해당 이름이 있는 경우
                score += yearning[name.index(j)]
        answer.append(score)
    return answer