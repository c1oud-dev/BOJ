test_case = int(input())
for t in range(1, test_case + 1):
    num = int(input())
    index = [0]*5
    while num > 1:
        if num % 2 == 0:
            num //= 2
            index[0] += 1
        elif num % 3 == 0:
            num //= 3
            index[1] += 1
        elif num % 5 == 0:
            num //= 5
            index[2] += 1
        elif num % 7 == 0:
            num //= 7
            index[3] += 1
        elif num % 11 == 0:
            num //= 11
            index[4] += 1

    print("#%d" %t, end=' ')
    for i in index:
        print(i, end=' ')
    print()
