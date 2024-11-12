def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # 두 값을 OR 연산한 후 n자리 2진수로 변환하여 #과 공백으로 매핑
        bin_str = format(i | j, f'0{n}b').replace('1', '#').replace('0', ' ')
        answer.append(bin_str)
    return answer
