'''
추월한 차량
'''
n = int(input()) #차량 수
car_in = [input().strip() for _ in range(n)]  # 들어가는 순서
car_out = [input().strip() for _ in range(n)]  # 나가는 순서

result = 0
car_in_dict = dict(zip(car_in, range(1, len(car_in) + 1)))  # 딕셔너리 생성
calc = []
for i in car_out:
    calc.append(car_in_dict[i])  # 나가는 차량 인덱스 저장

# 출구 순서에서 추월 여부 확인
for i in range(len(calc) - 1):
    for j in range(i + 1, len(calc)):
        if calc[i] > calc[j]:  # 뒤에 있어야 할 차량이 앞에 나오면 추월 발생
            result += 1
            break

# 최종 추월 횟수 출력
print(result)