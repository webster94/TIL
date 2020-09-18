dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())
for t in range(1,T+1):
    N = int(input())

# 초기값 정렬
    arr = [[0]*N for _ in range(N)]

    d = 0
    num = 1
    r = 0
    c = 0
    while(num <= N*N):
        arr[r][c] = num
        num += 1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r,c = nr, nc
        else:
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end = " ")
        print()
