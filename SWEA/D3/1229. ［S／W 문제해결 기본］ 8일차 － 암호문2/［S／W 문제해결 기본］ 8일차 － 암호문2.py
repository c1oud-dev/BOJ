'''
I 이면 삽입, D이면 삭제
'''
#import re  # swea 사용 불가
for test_case in range(1, 11):
    _ = int(input())
    origin = list(map(int, input().split()))
    _ = int(input())
    commands = input().replace("I", ";I").replace("D", ";D")  # I와 D를 기준으로 구분
    # ";"로 나눠 명령어 분리
    commands = commands.split(";")[1:]  # 첫 부분은 빈 문자열이므로 제외

    for i in commands:  # 첫 번째 인덱스는 공백이기 때문에 패스
        command = list(map(str, i.split()))  # 명령어 따로 저장

        #int_command = list(map(int, command[1:]))  # str 이므로 int 형으로 다시 변환
        # insert 와 delete 인걸 구분하려면 길이로 판단
        if command[0] == "I":  # insert 연산
            int_command = list(map(int, command[1:]))
            insert_position = int_command[0]  # 삽입할 위치
            insert_command = int_command[2:]  # 명령어 저장
            origin[insert_position:insert_position] = insert_command
        else:  #delete 연산
            int_command = list(map(int, command[1:]))
            del origin[int_command[0]:int_command[0] + int_command[1]]

    print(f"#{test_case} {' '.join(map(str, origin[:10]))}")