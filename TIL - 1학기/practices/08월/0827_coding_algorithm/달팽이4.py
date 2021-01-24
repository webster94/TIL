#이번엔 반대방향 달팽이를 만들어보까!
dr =[1,0,-1,0]
dc = [0,-1,0,1]
T = int(input())
for t in range(1,T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    d= 0
    r= 3
    c =3
    num =1
    while num < N*N:
        arr[r][c] = num
        num +=1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc] ==0:
            r,c = nr,nc
        else:
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print("#{}".format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end =' ')
        print()