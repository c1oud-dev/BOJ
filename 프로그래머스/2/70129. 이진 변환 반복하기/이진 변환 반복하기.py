def solution(s):
    zero, cnt = 0, 0  # 0의 개수, 변환 횟수

    while s != '1':
        cnt += 1
        zero += s.count('0')  # 0의 개수 추가
        s = bin(len(s.replace('0', '')))[2:]  # 0을 제거한 길이를 이진수로 변환

    return [cnt, zero]
