T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())  # 전선 개수
    wires = []
    
    # 전선 입력 받기
    for _ in range(N):
        A, B = map(int, input().split())
        wires.append((A, B))
    
    # 시작점 A 기준으로 정렬
    wires.sort()
    
    result = 0
    ends = []
    
    # 끝점 B 비교를 위한 리스트
    for _, B in wires:
        # 현재 끝점보다 큰 끝점 중 오른쪽에 있는 끝점을 찾아 교차 수 확인
        result += sum(1 for end in ends if end > B)
        
        # 끝점 리스트에 추가
        ends.append(B)
    
    print(f"#{test_case} {result}")