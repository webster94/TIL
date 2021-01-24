for t in range(1,11):
    N = int(input())
    li = [[int(x) for x in input().split()] for _ in range(100)] # 2차원배열 생성 (comprehension)
    sum_row = [0] * 100
    sum_col = [0] * 100
    sum_cross = [0]*2  # 빈배열 초기화
    for i in range(100):
        for j in range(100):  # 다스캔
            sum_row[i] += li[i][j]
            sum_col[i] += li[j][i]
            if i ==j:
                sum_cross[0] += li[i][j]
                sum_cross[1] += li[99-i][j]
    print(f'#{t} {max(max(sum_row),max(sum_col),max(sum_cross))}')