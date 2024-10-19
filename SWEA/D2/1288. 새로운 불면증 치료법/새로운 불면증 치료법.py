test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    nums = [-1]*10
    cnt = 1
    multi_n = n
    while True:
        multi_n = n * cnt
        num_list = list(map(int, str(multi_n))) #정수 분리
        for i in num_list:
            if i not in nums: #리스트에 특정 값이 없는지 체크
                nums[i] = i
        #0~9까지 모든 수가 있는지 확인
        if -1 in nums:
            cnt += 1
        else:
            break
    print("#%d %d" %(tc, multi_n))