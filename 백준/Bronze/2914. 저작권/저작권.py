'''
(창영이 앨범에 수록된 곡에 포함되어 있는 저작권이 있는 멜로디의 개수) / (앨범에 수록된 곡의 개수)
이때, 평균값은 항상 올림을 해서 정수로 만들어야 한다.

풀이
평균값 = 멜로디 개수 / 수록된 곡의 개수
평균값*수록된 곡의 개수 = 멜로디 개수
'''
#00:04 - 00:18

a, i = map(int, input().split())
print(a*(i-1)+1)