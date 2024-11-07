def solution(a, b, n):
    answer = 0
    while n >= a:
        new_bottles = (n // a) * b
        answer += new_bottles
        n = new_bottles + (n % a)
    return answer