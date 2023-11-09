'''
원본 문서의 너비가 10이고, 알파벳의 연속된 개수로 이루어져 있다.
압축된 문서 내용은 알파벳과 숫자로 구성되어 있고, 압축을 풀었을 때 그 개수대로 문서의 너비에 맞게 출력돼야 한다.

풀이
단순 구현
1. 문자열과 정수는 동시에 입력받을 수 없으므로 문자형으로 입력받고 정수는 정수형으로 치환
2. 한 리스트에 모두 저장
3. 10개를 넘어가면 다음 줄로 이동하여 출력
'''
#06:10 - #07:30 포기 / 17:47 - 18:15

t = int(input())

for i in range(1, t+1):
    n = int(input())
    alpha_list = [] #알파벳을 한 곳에 저장할 리스트
    for _ in range(n):
        alpha, num = input().split() #정수는 정수형으로 변환 필요
        value = alpha*int(num)
        alpha_list += value 
    cnt = 1
    print('#'+str(i))
    for ans in alpha_list:
        if cnt <= 10:
            print(ans, end='') #문자열 붙여주기
            cnt += 1
        if cnt > 10: #else로 하니깐 답이 이상하게 나온다.
            print()
            cnt = 1
    print() #추가