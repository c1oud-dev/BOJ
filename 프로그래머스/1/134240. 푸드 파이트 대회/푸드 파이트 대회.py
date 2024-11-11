def solution(food):
    answer = ''.join(str(foodNumber) * (quantity // 2) for foodNumber, quantity in enumerate(food))
    return answer + '0' + answer[::-1]
