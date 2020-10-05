dr = [0,1,0,-1]
dc = [1,0,-1,0]
def DFS(i,j):
    visited.append((i,j))
    global result
    if arr[i][j] == 3:
        result =1
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if nr < 0 or nc < 0 or nc >= N or nr >= N:
            continue
        elif arr[nr][nc] == 1:
            continue
        elif (nr,nc) in visited:
            continue
        DFS(nr,nc)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr= [list(map(int,input())) for _ in range(N)]
    visited = []
    result = 0
    for i in range(N):
        for j in range(N):
            st,en = -1,-1
            if arr[i][j] == 2:
                st,en = i,j
                DFS(st,en)
    print("#{} {}".format(t, result))
