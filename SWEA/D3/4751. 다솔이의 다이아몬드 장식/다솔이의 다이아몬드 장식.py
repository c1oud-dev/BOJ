'''
문자열이 주어지면 주위를 '#'으로 다이아몬드 형태로 감싸고 빈 곳은 '*'으로 5x5 크기로 장식한다.

규칙을 찾아야 함
'''
test_case = int(input())
for tc in range(test_case):
    word = input()
    length = len(word)
    line1 = '..#.'
    line2 = '.#'
    line3 = '#.'
    print(line1 * length + '.')
    print(line2 * length * 2 + '.')
    for i in range(length):
        print(line3 + word[i] + '.', end='')
    print('#')
    print(line2 * length * 2 + '.')
    print(line1 * length + '.')