def solution(A, B):
    answer = 0
    A.sort()  # 오름차순 정렬
    B.sort(reverse=True)  # 내림차순 정렬

    for i in range(len(A)):
        answer += A[i] * B[i]  # A의 최솟값 * B의 최댓값

    return answer