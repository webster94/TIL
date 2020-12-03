import sys
sys.stdin = open('연쇄폭발.txt','r')
dr = [1,0,0,-1]
dc = [0,1,-1,0]
def dfs(a,b):
    global cnt2
    q = []
    dist[a][b] = 2
    q.append((a,b))
    while q:
        a,b = q.pop(0)
        if a >=0 and b >=0:
            cnt2 += 1
            for k in range(4):
                nr = a + dr[k]
                nc = b + dc[k]
                cnt = 0

                while cnt < arr[a][b] and 0<= nr < N and 0 <= nc < N:
                    nr = nr +dr[k]
                    nc = nc +dc[k]
                    cnt +=1
                    if 0<= nr < N and 0 <= nc < N and arr[nr][nc] > 0 and not dist[nr][nc] :
                        if nr >= 0 and nc >= 0:
                            q.append((nr,nc))
                            dist[nr][nc] = 1




T = int(input())
for t in range(1,T+1):
    N = int(input())
    R,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    cnt = 0
    cnt2 = 0
    dfs(R,C)
    print(cnt2,dist)