def solution(n, words):
    game, cnt = 1, 1  # 게임 횟수, 차례
    end = words[0][-1]  # 첫 번째 단어 끝 저장
    used = [words[0]]  # 사용한 단어 저장
    for i in words[1:]:
        if cnt >= n:
            game += 1
            cnt = 1
        else:
            cnt += 1

        if i[0] != end or i in used:  # 끝말잇기 성립 확인/같은 단어 체크=
            return [cnt, game]

        end = i[-1]  # 마지막 글자 저장
        used.append(i)
    return [0, 0]