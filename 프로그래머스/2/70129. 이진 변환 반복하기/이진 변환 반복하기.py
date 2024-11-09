def solution(s):
    zero, num, cnt = 0, 0, 0  # 0의 개수, 2진법 길이, 변환 횟수

    while True:
        cnt += 1
        for i in s:
            if i == '1':
                num += 1
            else:
                zero += 1
        if num == 1:
            break
        else:
            s = format(num, 'b')
            num = 0
            
    return [cnt, zero]