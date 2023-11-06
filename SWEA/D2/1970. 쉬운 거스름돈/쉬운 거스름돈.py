'''
거스름돈을 최소 화폐로 거슬러줘야 한다.
5만원부터 10원까지 있다.

풀이 : 그리디, 단순 구현
'''
#15:25 - 15:48

t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def calc(n):
    for i in money:
        ans = 0
        if n >= i:
            ans = n // i #32850 / 10000 = 3
            n %= i # n = 2850
        print(ans, end= " ")

for i in range(1, t+1):
    n = int(input()) #거스름돈
    print("#"+str(i))
    calc(n)
    print()