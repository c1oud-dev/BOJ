test_case = int(input())
for tc in range(1, test_case + 1):
    month1, day1, month2, day2 = map(int, input().split())
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    month = month2 - month1
    day = 1
    if (month1 == month2):
        day += day2 - day1
    else:
        for i in range(month1 + 1, month2): #(4, 8) 4, 5, 6, 7
            day += days[i]
        day += days[month1] - day1 + day2
    print("#%d %d" %(tc, day))