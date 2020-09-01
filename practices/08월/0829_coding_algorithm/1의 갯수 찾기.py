# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def DFS(a,b):
    visited.append((a,b))
    global cnt #
    cnt +=1
    # 끝지점? 은 1을 모두 돌았을 경우!
    # 여기 잘몰겠다
    for c in range(4):
        nr = a +dr[c]
        nc = b + dc[c]
        if 0 < nr or 0 < nc or nr >= N or nc >= N or arr[nr][nc] != 1:
            continue
        elif (a,b) in visited:
            continue
        DFS(nr,nc)






N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# print(arr) # 입력받음
visited = []
cnt = 0
# dfs(재귀)를 이용하여 1의 개수를 확인하자
# 먼저 배열을 모두 탐색
for i in range(N):
    for j in range(N):
        st, en = -1, -1
        if arr[i][j] == 1:
            st,en = i,j
            DFS(st,en)
            print(cnt)