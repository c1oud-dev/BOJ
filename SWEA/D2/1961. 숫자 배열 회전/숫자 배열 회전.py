test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int, input().split())))
    print("#%d" %tc)
    east = [[0 for _ in range(n)] for _ in range(n)]
    north = [[0 for _ in range(n)] for _ in range(n)]
    west = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): 
        for j in range(n):
            east[i][j] = num_list[n-1-j][i] #90도
            north[i][j] = num_list[n-1-i][n-1-j] #180도
            west[i][j] = num_list[j][n-1-i] #270도
    
    for i in range(n): 
        print(*east[i], sep='', end=' ')
        print(*north[i], sep='', end=' ')
        print(*west[i], sep='')