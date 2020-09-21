import sys
sys.stdin = open("토마토.txt","r")
from _collections import deque
dr = [0,0,1,-1]
dc = [-1,1,0,0]
# q= deque()
# q.popleft()
def bfs(q):
    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            elif arr[nr][nc] == 1 or dist[nr][nc] != 0:
                continue
            elif arr[nr][nc] == -1:
                continue
            q.append((nr,nc))
            dist[nr][nc] = dist[r][c] + 1
            arr[nr][nc] = 1







M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
st,en = -1, -1
dist = [[0] * M for _ in range(N)]
q= deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
            arr[i][j] = 1
bfs(q)
dmax = 0
result = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = False
            break
        if dmax < dist[i][j]:
            dmax = dist[i][j]
if result == False:
    print(-1)
else:
    print(dmax)
