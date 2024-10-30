for test_case in range(1, 11):
    _ = int(input())
    origin = list(map(int, input().split()))
    _ = int(input())
    command = list(map(str, input().split("I")))  # I 구분자 기준으로 분리하여 저장
    
    for i in command:
        command_list = list(map(int, i.split()))  # 명령어를 한 줄씩 꺼내서 다시 따로 저장
        if len(command_list) == 0:  # 첫 번째 리스트는 비어있기 때문에 무시하는 코드 작성
            continue
        for j in range(command_list[1]):  
            origin.insert(command_list[0] + j, command_list[j + 2])  # 원하는 위치 i 앞에 추가할 값 x를 삽입
    
    result = origin[:10]  # 10번째까지만 출력

    print(f"#{test_case} {' '.join(map(str, result))}") 