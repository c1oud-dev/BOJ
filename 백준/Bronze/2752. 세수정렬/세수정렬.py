'''
정수 세 개를 생각한 뒤에, 이를 오름차순으로 정렬.
'''
#20:48 - 20:49
num = list(map(int, input().split()))
print(*sorted(num))