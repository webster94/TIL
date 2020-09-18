dr = [0,1,1,1,0,-1,-1,-1]
dc = [1,1,0,-1,-1,-1,0,1]
def DFS(i,j):
    visited.append((i,j))
    for d in range(8):
        nr = i + dr[d]
        nc = j + dc[d]

        if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc] == 0:
            continue
        if (nr,nc) in visited:
            continue
        DFS(nr, nc)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 입력 받음 나는 먼저 8방향으로 섬을 탐색한 후에
    # break하는 순간 카운트를 해서 섬의 개수를 표시하겠다. 최댓값을 최신화해서
    count = 0
    visited = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited and arr[i][j] != 0:
                DFS(i,j)
                count += 1
    print("#{} {}".format(t,count))

