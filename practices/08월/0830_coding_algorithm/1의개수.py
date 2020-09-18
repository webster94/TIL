N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# for

# def DFS(i,j):
#     visited.append((i,j))
#     print(visited)
#     global cnt
#     cnt += 1
#     for k in range(4):
#         nr,nc = i + dr[k], j +dc[k]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         elif arr[nr][nc] == 0:
#             continue
#         elif (nr,nc) in visited:
#             continue
#         DFS(nr,nc)


d = 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
cnt = 0
visited = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and (i,j) not in visited:
            while True:
                visited.append((i,j))
                cnt += 1
                nr = i + dr[d]
                nc = j + dc[d]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    continue
                elif arr[nr][nc] != 1:
                    continue
                elif (nr,nc) in visited:
                    continue
                else:
                    d = (d+1)%4
                    i += dr[d]
                    j += dr[d]
