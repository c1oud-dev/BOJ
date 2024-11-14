T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 주차 공간, 차량 수
    R = [int(input()) for _ in range(N)]  # 단위 무게당 금액
    W = [int(input()) for _ in range(M)]  # 차량 무게

    parking = [0]*N  # 주차장
    waiting = []  # 기다리고 있는 차량
    result = 0  # 주차 요금

    for _ in range(M * 2):
        car = int(input())  # 차량 출입 순서

        if car > 0:  # 들어오는 차량일 때
            if 0 not in parking:  # 주차 공간이 없으면 대기시키기
                waiting.append(car)
            else:
                for i in range(N):  # 주차 공간 탐색
                    if parking[i] == 0:  # 주차 공간이 비어있으면
                        parking[i] = car  # 주차 시키기
                        result += R[i] * W[car - 1]  # 요금 계산
                        break

        else:  # 나가는 차량일 때
            now_idx = parking.index(abs(car))  # 나가는 차량 인덱스
            parking[now_idx] += car  # 해당 차량이 들어있는 인덱스 찾아서 0으로 만들기
            if len(waiting) != 0:  # 대기하고 있는 차량이 있을 때 주차시키기
                waiting_car = waiting.pop(0)
                parking[now_idx] = waiting_car  # 주차시키기
                result += R[now_idx] * W[waiting_car - 1]  # 요금 계산

    print(f"#{test_case} {result}")