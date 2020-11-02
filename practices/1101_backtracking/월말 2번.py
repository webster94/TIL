import sys
sys.stdin = open('월말2번.txt','r')
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def bfs(a,b):
    dist[a][b] = 1
    global cnt
    cnt +=1
    q = []
    q.append((a,b))
    while q:
        a,b = q.pop(0)
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0<=nr< N and 0 <= nc < M and arr[nr][nc] and not dist[nr][nc]:
                dist[nr][nc] = 1
                q.append((nr,nc))

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split()) # 세로 , 가로
    arr = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        st,ed = map(int,input().split())
        arr[st][ed] = 1
    dist = [[0]*(M) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not dist[i][j] :
                bfs(i,j)
    print(cnt)