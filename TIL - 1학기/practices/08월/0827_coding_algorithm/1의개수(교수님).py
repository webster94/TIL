dr = [-1,1,0,0]  # 위아래좌우
dc = [0,0,-1,1]
def DFS(r,c):
    global cnt
    arr[r][c] = 0
    cnt +=1 # 여기들어왔다는건 count +1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0:
            continue
        DFS(nr,nc)


N = int(input())

arr = [list(map(int,input())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            DFS(i,j)
            print(cnt)

# 7
# 0000000
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000