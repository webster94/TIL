import sys
sys.stdin = open("단지번호.txt","r")
from _collections import deque
def bfs(a,b):
    global num
    num +=1
    q = deque()
    q.append((a,b))
    dist[a][b] = num
    count = 1
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = num
                count +=1
                q.append((nr,nc))
    result.append(count)

dr = [0,0,-1,1]
dc = [-1,1,0,0]
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
dist = [[0] * N for _ in range(N)]
num = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            bfs(i,j)

print(num)
result.sort()
for i in result:
    print(i)
# bin = {}
# for i in dist:
#     for j in i:
#         bin[j] = bin.get(j,0)+1
# print(int(num))
# for i in range(1,num+1):
#     print(int(bin[i]))
# print(dist)