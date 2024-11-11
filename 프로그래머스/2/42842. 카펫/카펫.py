def solution(brown, yellow):
    square = brown + yellow
    for i in range(1, int(square**0.5) + 1):
        if square % i == 0:
            width = square // i
            height = i
            if (width - 2) * (height - 2) == yellow:
                return [width, height]