import sys
sys.stdin = open('토마토.txt','r')

dr = [0,0,1,-1]
dc = [-1,1,0,0] # 우 상 좌 하
def BFS(q):

    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 > nr or 0 > nc or N <= nr or M <= nc :  #  범위 벗어나걱나
                continue
            elif arr[nr][nc] == 1 or dist[nr][nc] != 0:  #arr 이 1이거나 방문한 흔적이 있다면 continue
                continue
            elif arr[nr][nc] == -1:   # -1이 아니면
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append((nr,nc))
            arr[nr][nc] = 1  # 방문
M,N = map(int,input().split()) # M은 가로, N은 세로
arr = [list(map(int,input().split())) for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
dist = [[0]*M for _ in range(N)]
BFS(q)
maxi = 0
temp = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            temp = True

        elif maxi <= dist[i][j]:
            maxi = dist[i][j]
if temp :
    print(-1)
else:
    print(maxi)
print(dist)
