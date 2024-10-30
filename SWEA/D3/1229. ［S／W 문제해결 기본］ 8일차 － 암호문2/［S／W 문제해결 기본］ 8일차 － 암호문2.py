'''
I 이면 삽입, D이면 삭제
'''
for test_case in range(1, 11):
    _ = int(input())  # 원본 암호문 길이
    origin = list(map(int, input().split()))  # 원본 암호문
    _ = int(input())  # 명령어 개수
    commands = input().replace("I", ";I").replace("D", ";D")  # I와 D로 구분하여 명령어 분리
    commands = commands.split(";")[1:]  # 빈 첫 부분 제외

    for i in commands:
        command = i.split()  # 명령어 분리
        cmd_type, x, y = command[0], int(command[1]), int(command[2])

        if cmd_type == "I":  # insert 연산
            s = map(int, command[3:])  # 삽입할 숫자들
            origin[x:x] = s  # 리스트 슬라이싱으로 한번에 삽입
        elif cmd_type == "D":  # delete 연산
            del origin[x:x + y]  # 리스트 슬라이싱으로 삭제

    print(f"#{test_case} {' '.join(map(str, origin[:10]))}")