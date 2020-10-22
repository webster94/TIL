import sys
sys.stdin = open('토마토.txt','r')
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def BFS(q):
    while(q):
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            elif arr[nr][nc] == 1 or dist[nr][nc] != 0: # 방문체크
                continue
            elif arr[nr][nc] == -1:
                continue
            q.append((nr,nc))
            dist[nr][nc] = dist[r][c] +1
            arr[nr][nc] = 1
T = int(input())
for t in range(1,T+1):
    M,N = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [ [0] * M for _ in range(N)]

    #1찾기
    q= []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
    BFS(q)
    maxi = 0
    flag = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 :
                flag = False
                break
            elif maxi <= dist[i][j]:
                maxi = dist[i][j]
    if flag :
        print(maxi)
    else:
        print(-1)