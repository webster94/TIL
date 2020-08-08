N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for x in range(0, N-M+1):
    for y in range(0,N-M+1): # (x,y)이고 크기가 M인 사각영역을 처리

       S = 0
        for i in range(x,x+M):
            for j in range(y,y+M):
                S += arr[i][j]

                