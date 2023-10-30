#22:02-22:07
#풀이 - 리스트를 정렬한 후 인덱스의 중간값 찾기

n = int(input())
num = list(map(int, input().split()))
num.sort()
print(num[n//2])