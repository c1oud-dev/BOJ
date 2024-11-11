def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] >= 2:  # 2로 나눠야 하므로 2보다 커야 한다.
            for j in range(food[i] // 2):
                answer += str(i)

    return answer + '0' + answer[::-1]
