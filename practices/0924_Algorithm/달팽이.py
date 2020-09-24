import sys
sys.stdin = open("달팽이.txt","r")
dr = [0,1,0,-1]
dc = [1,0,-1,0]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]
    num = 0
    d = 0
    r,c = 0,0
    while num < N*N:
        num +=1
        arr[r][c] = num
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<= nr< N and 0<= nc< N and arr[nr][nc] ==0:
            r,c = nr,nc
        else:
            d = (d+1)%4
            r += dr[d]
            c += dc[d]
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end = ' ')
        print()

