test_case = int(input())
for tc in range(1, test_case + 1):
    a, b = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    min_list = min(aList, bList, key=len) 
    max_list = max(aList, bList, key=len) 
    max_sum = 0
    cnt = 0
    while cnt <= len(max_list) - len(min_list):
        sum = 0
        for i in range(len(min_list)):
            sum += min_list[i] * max_list[i + cnt] #곱한 뒤 합계
        max_sum = max(max_sum, sum) #최대값 저장
        cnt += 1

    print("#%d %d" %(tc, max_sum))