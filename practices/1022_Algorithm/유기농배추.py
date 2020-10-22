import sys
sys.stdin = open('유기농배추.txt','r')
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def bfs(a,b):
    global count
    count +=1
    q.append((a,b))
    dist[a][b] = 1
    while q:
        r,c = q.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nc < 0 or nr >= M or nc >= N:
                continue
            elif arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue
            q.append((nr,nc))
            dist[nr][nc] = 1



T = int(input())
for t in range(1,T+1):
    M,N,K = map(int,input().split()) # 가로,세로,위치개수
    arr = [[0]*(N) for _ in range(M)]
    for _ in range(K):
        x,y = map(int,input().split())
        arr[x][y] = 1
    count = 0
    q =[]
    dist = [[0]*(N) for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and dist[i][j] == 0:
                bfs(i,j)
    print(count)