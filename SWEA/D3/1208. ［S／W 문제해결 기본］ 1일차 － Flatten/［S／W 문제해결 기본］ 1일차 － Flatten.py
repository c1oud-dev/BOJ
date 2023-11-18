'''
23:27 - 00:08
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄인다.
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환한다.
가로 길이는 항상 100이다.

풀이
max와 min을 쓰면서 반복, or 정렬?
'''
for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    top = 0
    bottom = 0
    for i in range(dump+1):
        top = max(box)
        bottom = min(box)
        
        box.remove(top)
        box.remove(bottom)
        if i == dump: #if문 없으면 마지막에 한 번 더 덤프하기 때문에 추가
            break
        elif top == bottom:
            top += 1
            bottom -= 1
            break
        else:
            #덤프
            top -= 1
            bottom += 1
            #print(top, bottom)

            box.append(top)
            box.append(bottom)

    print('#'+str(tc), top-bottom)
#1차 제출 실패 - 테스트 파일 중 9개 맞음, 반례가 있는 듯
#문제 다시 읽어보니 덤프 횟수 이내에 평탄화가 완료되면 수행할 수 없으므로 그 때의 최고점과 높이 차를 반환해야 한다고 한다.