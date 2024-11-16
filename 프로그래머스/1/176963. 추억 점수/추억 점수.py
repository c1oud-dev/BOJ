def solution(name, yearning, photo):
    # 이름과 그리움 점수를 딕셔너리로 매핑
    yearning_dict = dict(zip(name, yearning))
    
    answer = []
    for people in photo:
        # 각 사진 속 인물의 점수를 계산
        score = sum(yearning_dict.get(person, 0) for person in people)
        answer.append(score)
    
    return answer