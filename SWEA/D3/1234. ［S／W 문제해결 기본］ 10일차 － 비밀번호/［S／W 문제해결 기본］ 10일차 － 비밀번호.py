'''
06:26 - 07:05
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만들어야 한다.
'''

def calc(password):
    for i in range(1, len(password)):
        if password[i-1] == password[i]:
            #del password[i-1:i]
            password.pop(i)
            password.pop(i-1)
            return calc(password)
            #break
    return password

for tc in range(1, 11):
    n, password = map(int, input().split())
    word = []
    print('#'+str(tc), end=' ')
    for i in str(password):
        word.append(i)
    word = calc(word)
    if word[0] == '0':
        word.pop(0) #pop은 인덱스 삭제
    for j in word:
        print(j, end='')
    print()
#1차 제출 실패 - 마지막 테스크 케이스 결과에 09823 이라고 나오는데 올바른 답은 9823이다.