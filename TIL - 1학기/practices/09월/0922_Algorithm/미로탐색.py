import sys
sys.stdin = open("미로탐색.txt","r")
from _collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]
def BFS(a,b):
    dist[a][b] = 1
    q = deque()
    q.append((a,b))
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            elif arr[nr][nc] == 0:
                continue
            elif dist[nr][nc] !=0: # dist가 0이 아니면 가지말 것
                continue
            q.append((nr,nc))
            dist[nr][nc] = dist[r][c] +1



N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]
BFS(0,0)
print(dist[N-1][M-1])