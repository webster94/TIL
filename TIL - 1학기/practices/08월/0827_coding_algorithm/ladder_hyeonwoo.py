# 입력을 받는다. O
# 도착지를 찾는다. O
# 도착지에서부터 거슬러 올라가는 DFS함수를 만들어서 쓴다.
# 인쇄

di = [0,0,-1] # 왼,오, 위
dj = [-1,1,0]

def DFS(i,j):
    board[i][j] = 0
    if i == 0:
        return j
    # 가려는 곳이 배열 밖이면 안됨
    # 가려는 곳이 1이어야 댐
    # 왼쪽,오른쪾을 먼저 봐야대
    for k in range(3):
        ni,nj = i+di[k], j+dj[k]
        if ni < 0 or nj < 0 or ni >= 100 or nj >= 100:
            continue
        if board[ni][nj] != 1:
            continue
        # 다른 방법
        # if ni >= 0 and nj >= 0 and ni < 100 and nj < 100 and board[ni][nj] == 1:
        #     DFS
        return DFS(ni,nj)

for tc in range(1,11):
    num = input()
    board = [list(map(int,input().split())) for _ in range(100)]
    si,sj = -1,-1
    for j in range(100):
        if board[99][j] == 2:
            si,sj = 99,j
    print(DFS(si,sj))