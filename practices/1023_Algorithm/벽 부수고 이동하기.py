import sys
sys.stdin = open('벽부수기.txt','r')
from collections import deque
dr = [0,0,1,-1] # 좌우하상
dc = [1,-1,0,0]
def bfs():
    q = deque()
    q.append((0,0,1))
    visit = [[[0] * 2 for i in range(M)] for i in range(N)]
    visit[0][0][1] = 1
    while q:
        r,c,w = q.popleft()
        if (r,c) == (N-1,M-1):
            return visi[r][c][w]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and w ==1:
                    visit[nr][nc][0] = visit[r][c][1] + 1
                    q.append((nr,nc,0))
                elif arr[nr][nc] == 0 and visit[nr][nc][w] == 0:
                    visit[nr][nc][w] = visit[r][c][w] + 1
                    q.append((nr,nc,w))
    return -1


N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
dist = [[0] * (M) for _ in range(N)]
print(bfs())
# print(dist)