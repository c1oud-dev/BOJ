'''
오늘의 요일을 나타내는 문자열 s가 주어짐
일요일까지 며칠 남았는지 출력
'''
test_case = int(input())
for tc in range(1, test_case + 1):
    day = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    result = 0
    for i in range(len(days)):
        if days[i] == day:
            result = 7 - i
            break
    print("#%d %d" %(tc, result))