import sys
input = sys.stdin.readline

n = int(input()) #단어 개수
word = [] #단어를 입력받아서 담을 리스트

for _ in range(n): #단어 입력받기
    word.append(input().rstrip())

dict = {}
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in dict:
            dict[word[i][j]] += 10**(len(word[i])-j-1)
        else:
            dict[word[i][j]] = 10**(len(word[i])-j-1)

alpha = []
for i in dict.values(): #values() key의 value를 얻기 위함
    alpha.append(i)
alpha.sort(reverse=True) #내림차순 정렬, 디폴트값이 오름차순

sum = 0
max = 9
for i in alpha:
    sum += i*max
    max -= 1
print(sum)