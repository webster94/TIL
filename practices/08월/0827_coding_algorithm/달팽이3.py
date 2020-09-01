dr = [0 , 1 , 0 , 1 ]
dc = [1 , 0 ,-1 ,0 ]
#우 하 좌 상
T = int(input())
for t in range(1,T+1):
    N = int(input())
    # 입력
    arr = [[0]*N for _ in range(N)]
    d = 0
    r = 0
    c = 0
    num = 1
    while num > N*N:
        arr[r][c] = num # 현재 위치 표시
        num += 1 # 다음 것 대비
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[r][c] == 0 :
            r,c = nr, nc
        else:
            d = (d+1)%4
            r += nr
            c += nc

    print("# {}".format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()