import sys; sys.stdin = open("미로1.txt","r")
# 입력받기
# 출발점 찾고
# 출발!
# 0을 따라 이동 방향 우 하 좌 상
# 도착하면 1 못하면 0
dr = [0,1,0,-1]
dc = [1,0,-1,0]
def DFS(a,b):
    visited.append((a, b))  # 방문을 튜플로 처리
    global ans
    if arr[a][b] == 3:
        ans =1
        return ans

    for k in range(4):
        nr = a + dr[k]
        nc = b + dc[k]
        if nr < 0 or nc < 0 or nc >= 16 or nr >= 16:
            continue
        if arr[nr][nc] == 1:
            continue
        if (nr,nc) in visited:
            continue
        DFS(nr,nc)
for tc in range(1,11):
    N = int(input())
    arr= [list(map(int,input())) for _ in range(16)]
    # 미로 형성완료
    # 출발점 찾기
    visited = []
    for i in range(16):
        for j in range(16):
            ans = 0
            st,en = -1,-1
            if arr[i][j] ==2:
                st,en = i,j # 모두다 1,1 이넹
                ans = DFS(st,en)
                print("#{} {}".format(tc,ans))
