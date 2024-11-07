def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        divisor_cnt = 0
        # 약수 개수 계산을 1부터 sqrt(i)까지만 진행
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisor_cnt += 1
                if j != i // j:  # 제곱수가 아닌 경우에만 다른 쌍을 추가
                    divisor_cnt += 1
                
            if divisor_cnt > limit:  # 제한 수치를 초과하면 중단
                divisor_cnt = power
                break

        answer += divisor_cnt if divisor_cnt <= limit else power

    return answer