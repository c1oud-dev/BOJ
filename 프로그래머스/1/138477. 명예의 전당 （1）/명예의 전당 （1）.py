import heapq

def solution(k, score):
    hall_of_fame = []  # 명예의 전당 (최소 힙)
    result = []

    for s in score:
        heapq.heappush(hall_of_fame, s)  # 점수 추가
        if len(hall_of_fame) > k:  # 크기 초과 시 최소값 제거
            heapq.heappop(hall_of_fame)
        result.append(hall_of_fame[0])  # 현재 명예의 전당의 최하위 점수 기록

    return result