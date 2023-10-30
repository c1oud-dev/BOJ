a, b = map(int, input().split())
rock = 2
scissors = 1
paper = 3
#주먹을 냈을 때 이기는 건 보, 가위를 냈을 때 이기는 건 주먹, 보를 냈을 때 이기는 건 가위
if a == rock:
    if b == scissors:
        print("A")
    else:
        print("B")
elif a == scissors:
    if b == paper:
        print("A")
    else:
        print("B")
else:
    if b == rock:
        print("A")
    else:
        print("B")