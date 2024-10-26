'''
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부텅 차례로 정렬하여 출력

딕셔너리 사용
'''
T = int(input())
for test_case in range(1, T + 1):
    tc, tc_len = map(str, input().split())
    nums = list(map(str, input().split()))
    planet_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    planet_dict = dict(zip(planet_nums, range(len(planet_nums))))  # list to dict
    value_list = []
    for key in nums:
        value_list.append(planet_dict[key])  # 키로 값에 접근해서 값만 저장
    value_list = sorted(value_list)
    # 리스트 인덱스에 맞게 출력
    result = []
    print(f"#{test_case}")
    for i in value_list:
        print(f"{planet_nums[i]}", end=' ')
    print()