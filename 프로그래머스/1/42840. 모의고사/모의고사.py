def correct(student_answer, answers):
    return sum(1 for i, ans in enumerate(answers) if ans == student_answer[i % len(student_answer)])

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [correct(pattern, answers) for pattern in patterns]
    max_score = max(scores)
    
    return [i + 1 for i, score in enumerate(scores) if score == max_score]
