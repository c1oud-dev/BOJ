def solution(s):
    answer = []
    last_seen = {}  # 각 문자의 마지막 위치를 저장하는 딕셔너리
    
    for i, char in enumerate(s):
        if char in last_seen:
            # 이전에 등장했다면, 현재 위치와 이전 위치의 차이를 계산
            answer.append(i - last_seen[char])
        else:
            # 이전에 등장하지 않았다면 -1 추가
            answer.append(-1)
        # 현재 위치를 마지막 위치로 갱신
        last_seen[char] = i
    return answer