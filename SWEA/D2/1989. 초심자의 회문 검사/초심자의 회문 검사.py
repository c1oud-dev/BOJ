'''
level과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라고 한다.
단어를 입력 받아 회문이면 1을 출력, 아니면 0을 출력한다.
단어의 길이는 3 이상 10 이하이고, 공백은 없다.

풀이
1. 단어를 입력 받는다.
2. 반복문을 통해 단어를 거꾸로 하나씩 꺼낸다. 아니면 리스트 변환 후 sort(reverse=true)
3. 입력 받은 단어와 같은지 판단
'''
#16:00 - 16:06

t = int(input())

for i in range(1, t+1):
    word = input()
    revision = ''
    for w in word[::-1]:
        revision += w
    if word == revision:
        print('#'+str(i), '1')
    else:
        print('#' + str(i), '0')