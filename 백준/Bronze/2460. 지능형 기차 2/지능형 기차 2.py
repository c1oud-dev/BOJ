'''
 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다.
 사람이 가장 많을 때의 사람 수를 계산
'''
get_off, get_on = [], []
for _ in range(10):
    off, on = map(int, input().split())
    get_off.append(off)
    get_on.append(on)
    
result, max_on = 0, 0
for off, on in zip(get_off, get_on):
    max_on -= off
    max_on += on
    result = max(result, max_on)
print(result)