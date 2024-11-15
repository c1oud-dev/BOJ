def solution(k, score):
    answer = []
    top = []

    for s in score:
        top.append(s)
        if len(top) > k:  # 명예의 전당 크기를 초과하면 최소값 제거
            top.remove(min(top))
        answer.append(min(top))  # 현재 명예의 전당의 최하위 점수 기록

    return answer