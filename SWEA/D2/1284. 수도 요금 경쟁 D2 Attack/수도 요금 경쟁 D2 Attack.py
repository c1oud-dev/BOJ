test_case = int(input())

def A(p, w):
    #1리터당 p원
    return p * w

def B(q, r, s, w):
    #r리터 이하이면 q원, 이상이면 초과량에 대해 1리터당 s원
    if w <= r:
        return q
    else:
        return q + (s * (w - r))

for t in range(1, test_case + 1):
    p, q, r, s, w = map(int, input().split())
    a = A(p, w)
    b = B(q, r, s, w)
    if a < b:
        print("#%d %d" %(t, a))
    else:
        print("#%d %d" %(t, b))