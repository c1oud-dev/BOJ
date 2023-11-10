'''
NxN 크기의 단어 퍼즐에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력한다.
검은색으로 칠해진 곳은 단어가 들어갈 수 없다. 흰색으로 칠해진 곳에만 넣을 수 있다. 검은색 = 0, 흰색 = 1
가로 혹은 세로로 단어를 놓을 수 있다. 단어의 길이와 픽셀수는 같아야 한다.

풀이
그래프 탐색 알고리즘을 굳이 쓸 필요는 없을 것 같다.
'''
#17:13 - 18:25

t = int(input())
def calc(puzzle):
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            else:  # 0일 때, 만약 7x7 퍼즐에서 단어가 3자리일 때 가로에서 2가지가 나올 수 있기 때문
                if cnt == k:  # 카운트값과 단어 자릿수랑 맞으면
                    ans += 1  # 결과값에 1을 더하고
                    cnt = 0  # 카운트값 초기화
                else:  # 카운트값과 단어 자릿수랑 맞지 않으면
                    cnt = 0  # 결과값은 무시하고, 카운트값 초기화
        if cnt == k:
            ans += 1
    return ans

for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    ans += calc(puzzle) #가로
    ans += calc(list(zip(*puzzle))) #세로
    print('#'+str(tc), ans)
#1차 제출 실패 - input 파일 중 6개만 맞았음, 조건부 수정하고 2차 제출 후 성공