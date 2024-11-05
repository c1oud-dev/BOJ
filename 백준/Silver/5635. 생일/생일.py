'''
학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하라
'''
from datetime import date

n = int(input())  # 학생의 수
students = []
for _ in range(n):
    students.append(list(map(str, input().split())))

min_compare = date(1990, 1, 1)
max_compare = date(2010, 12, 31)
result1 = ""
result2 = ""
for name, day, month, year in students:
    age = date(int(year), int(month), int(day))  # 지정 날짜
    if age > min_compare:
        min_compare = age
        result1 = name
    if age < max_compare:
        max_compare = age
        result2 = name

print(result1)
print(result2)