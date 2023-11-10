'''
NxN 크기의 단어 퍼즐에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력한다.
검은색으로 칠해진 곳은 단어가 들어갈 수 없다. 흰색으로 칠해진 곳에만 넣을 수 있다. 검은색 = 0, 흰색 = 1
가로 혹은 세로로 단어를 놓을 수 있다. 단어의 길이와 픽셀수는 같아야 한다.

풀이
그래프 탐색 알고리즘을 굳이 쓸 필요는 없을 것 같다.
'''
#17:13 - 18:05

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    #가로 확인
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            else: #수정한 부분
                if cnt == k:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == k:
            ans += 1

    #세로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            else: #수정한 부분
                if cnt == k:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == k:
            ans += 1
    print('#'+str(tc), ans)
#1차 제출 실패 - input 파일 중 6개만 맞았음,