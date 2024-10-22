'''
b, d, p, q로 이루어진 문자열이 있다. 이 문자를 거울에 비추면 어떤 문자열이 되는지 구하라
예를 들어 bdppq를 거울에 비치면 pqqbd처럼 나타난다.

문자열을 reverse() 한 후 b와 d 반대로, p와 q도 replace()를 사용하여 반대로 출력하는 방법
for 문 이용해서 결과값에 누적
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    word = input()
    #word = word[::-1] #문자열도 리스트라고 생각하자
    result = ""
    for i in word:
        if i == "b":
            result += "d"
        elif i == "d":
            result += "b"
        elif i == "q":
            result += "p"
        else:
            result += "q"

    print("#%d %s" %(tc, result[::-1]))