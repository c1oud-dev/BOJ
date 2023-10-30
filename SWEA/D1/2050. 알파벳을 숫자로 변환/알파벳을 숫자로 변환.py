#21:40 - 21:46

alpha = input()
for i in alpha: #string이라 하나씩 꺼내기 가능
    print(ord(i)-64, end = " ") #ord : 알파벳을 아스키코드로 치환, 대문자는 65부터, 소문자는 97부터