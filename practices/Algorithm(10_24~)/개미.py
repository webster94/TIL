import sys
sys.stdin = open('개미.txt','r')

dr = [1,-1,1,-1]  # 상좌, 상우 , 좌하, 우하
dc = [1,-1,-1,1]

def bfs(a,b,cnt):
    q = [(a,b)]
    visited[a][b] = 1
    while q :
        r,c = q.pop(0)
        print(r,c,cnt)
        if cnt == 0:
            return r,c
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while cnt > 0 and 0 <= nr < h and 0<= nc < w and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                nr,nc = nr +dr[i] ,nc + dc[i]
                q.append((nr, nc))
                cnt -= 1


w,h = map(int,input().split())
p,q = map(int,input().split())
cnt = int(input())
visited = [[0] * (w+1) for _ in range(h+1)]
print(bfs(p,q,cnt))
print(visited)