'''
기다린 시간을 분 단위로 출력한다.
11일 11시 11분 이하이면 -1 을 출력
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    D, H, M = map(int, input().split())
    
    # 기준 시간: 2011년 11월 11일 11시 11분을 분 단위로 변환
    base_minutes = (11 * 24 * 60) + (11 * 60) + 11  # 기준 날짜 시간 분
    # 입력받은 시간 (D일 H시 M분)도 분 단위로 변환
    current_minutes = (D * 24 * 60) + (H * 60) + M

    # 경과 시간 계산
    if current_minutes < base_minutes:
        result = -1
    else:
        result = current_minutes - base_minutes
    
    print(f"#{test_case} {result}")