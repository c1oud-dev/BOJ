def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0  # 공격력 초기화
        for j in range(1, int(i**0.5) + 1):  # 약수 확인
            if i % j == 0:  # 약수
                cnt += 1  # 약수 개수
                if i // j != j:  # 몫과 나누는 수와 같다면 무시(6 x 6) 일 때
                    cnt += 1
        #무기 구매
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer