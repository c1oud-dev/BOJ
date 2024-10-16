test_case = int(input())

def hour_calc(hour):
    if hour > 12:
        hour -= 12
        hour_calc(hour)

    return hour

def minute_calc(hour, minute):
    if minute > 60:
        minute -= 60
        hour += 1
        hour = hour_calc(hour)
        minute_calc(hour, minute)

    return hour, minute

for tc in range(1, test_case + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split())
    hour = hour1 + hour2
    minute = minute1 + minute2
    while hour > 12:
        hour -= 12 
    hour, minute = minute_calc(hour, minute)

    print("#%d %d %d" %(tc, hour, minute))