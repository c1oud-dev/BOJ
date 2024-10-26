'''
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부텅 차례로 정렬하여 출력

딕셔너리 사용
'''
#Refactoring
# 행성의 숫자 단어와 순서를 매핑
planet_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
order_dict = {word: index for index, word in enumerate(planet_numbers)}


# 입력된 문자열 리스트를 정렬하는 함수
def sort_planet_numbers(words):
    # 각 단어를 order_dict의 값(숫자)에 따라 정렬
    sorted_words = sorted(words, key=lambda word: order_dict[word])
    # 결과를 공백으로 연결하여 반환
    return ' '.join(sorted_words)


# 테스트 케이스 실행
T = int(input())
for test_case in range(1, T + 1):
    input()  # 테스트 케이스 번호와 길이를 받는 줄은 생략
    nums = input().split()  # 숫자 문자열 리스트 입력
    sorted_string = sort_planet_numbers(nums)
    print(f"#{test_case}")
    print(sorted_string)