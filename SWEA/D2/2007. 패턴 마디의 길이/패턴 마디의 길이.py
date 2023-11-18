'''
00:50 - 01:27
반복되는 마디의 길이를 출력한다. 문자열의 길이는 30이고, 마디의 최대 길이는 10이다.
마디의 최대 길이가 제한적이므로 이걸 이용한다.
뒤에서부터?
'''
t = int(input())
for tc in range(1, t+1):
    word = input()
    ans = 0
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                if word[i:j-1] == word[j:2*j]:
                    ans = len(word[i:j-1])+1
    print('#'+str(tc), ans)