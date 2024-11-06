def correct(student_answer, answers):
    cnt, j = 0, 0
    for i in range(len(answers)):
        if answers[i] == student_answer[j]:
            cnt += 1
        j += 1
        if j >= len(student_answer):
            j = 0

    return cnt

def solution(answers):
    answer = []

    one = correct([1, 2, 3, 4, 5], answers)
    two = correct([2, 1, 2, 3, 2, 4, 2, 5], answers)
    three = correct([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answers)
    cnt = [one, two, three]
    max_cnt = max(cnt)
    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i + 1)

    return answer