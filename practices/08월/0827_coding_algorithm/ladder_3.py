# 입력을 받고
# 시작 지점에서
# 끝지점을 으로 가는 dfs를 만들자. 재귀로!
dr = [0,0,-1]
dc = [-1,1,0]
def DFS(i,j):
    # 재귀함   수에서 중요한 종료조건!
    arr[i][j] = 0
    if i == 0:
        return j
    for a in range(3): # 방향지정
        nr = i+ dr[a]
        nc = j+ dc[a]
        if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] ==1:
            return DFS(nr,nc)


        # 종료조건이 밖을 나가면 안되고 n  = 1이 아니면 안돼
        #

for i in range(1,11):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    st = -1
    en = -1
    for i in range(100):
        if arr[99][i] == 2:
            st, en = 99, i

    # 시작지점 찾았음!
    a= DFS(st,en)
    print(a)
