import sys; sys.stdin = open("미로의거리.txt","r")
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def BFS(i,j):
    q = [(i,j)]
    dist[i][j] = 0 # 방문처리
    while len(q) > 0:
        curr_r, curr_c = q.pop(0)  # r,c에 값을 넣어준다.
        for k in range(4):
            nr = curr_r + dr[k]
            nc = curr_c + dc[k]
            if nr < 0 or nc <0 or nc >= N or nr >= N or arr[nr][nc] == 1: # 1은 벽이니까 가면안됨
                continue
            if dist[nr][nc] != 0: # 디스트가 0이 아니면 가지말 것
                continue
            if arr[nr][nc] == 3: # 정답을 찾았으면 그곳에 동일한 값을 저장한다
                dist[nr][nc] = dist[curr_r][curr_c]
                return dist[nr][nc] # 저장된 값을 리던

            q.append((nr,nc))  # nr,nc
            dist[nr][nc] = dist[curr_r][curr_c]+1





T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]  # DSF와의 차이
    for i in range(N):
        for j in range(N):
            st,en = -1,-1
            if arr[i][j] == 2 and dist[i][j] == 0 :
                st,en = i,j
                print(BFS(i,j))
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] ==3:
    #             print("#{} {}".format(t,dist[i][j]))