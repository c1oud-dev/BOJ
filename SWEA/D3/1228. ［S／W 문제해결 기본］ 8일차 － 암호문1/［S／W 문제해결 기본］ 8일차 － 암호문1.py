for test_case in range(1, 11):
    _ = int(input())
    origin = list(map(int, input().split()))
    _ = int(input())
    command = input().split("I")[1:]  # 첫 번째 빈 요소를 제거하고 시작

    for i in command:
        command_list = list(map(int, i.split()))
        insert_position = command_list[0]
        num_to_insert = command_list[2:]
        
        # 해당 위치에 명령어대로 값 삽입
        origin[insert_position:insert_position] = num_to_insert

    # 10번째까지만 출력
    result = origin[:10]
    print(f"#{test_case} {' '.join(map(str, result))}")