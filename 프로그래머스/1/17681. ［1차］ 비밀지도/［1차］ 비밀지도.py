def solution(n, arr1, arr2):
    answer = []
    # 배열 2진수로 변환, 한 줄 씩
    for i, j in zip(arr1, arr2):
        bin_str = ''
        for first, second in zip(format(i, f'0{n}b'), format(j, f'0{n}b')):
            for f, s in zip(first, second):
                if f == '1' or s == '1':
                    bin_str += '#'
                else:
                    bin_str += ' '
        answer.append(bin_str)
    return answer