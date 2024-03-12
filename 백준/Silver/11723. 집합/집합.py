'''
비어있는 공집합 S가 주어졌을 때
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다
'''
#22:34 - 22:59(03-10 일단 포기) 16:23 - 17:18

import sys
input = sys.stdin.readline

m = int(input())
s = [] #공집합
for _ in range(m):
    num = input().strip() #1. 문자형으로 입력 받기
    #comm_x = list(map(str, num)) #map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 합니다.
    #공백 때문에 숫자 문자 판별이 안 됨
    #num_re = num.replace(" ","") #strip()은 양 끝만 제거되므로 replace()
    #num = num.strip()
    if num.isalpha() == True: #문자만 있으면(공백이 없으면)
        if num == 'all':
            s = [0]*20 #이렇게 안 해주면 out of range 뜸
            for i in range(20):
                s[i] = i+1
        if num == 'empty':
            s = []

    if num.isalpha() == False: #공백이 있으면
        comm, x = num.split()  # 공백을 기준으로 나누기
        x = int(x)
        if comm == 'add' and x not in s:  # 명령어가 add일 때 x가 없는 경우 x를 공집합에 추가
            s.append(x)
        if comm == 'remove' and x in s:  # 명령어가 remove일 때 x가 있는 경우 x를 공집합에서 제거
            s.remove(x)
        if comm == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        if comm == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.append(x)