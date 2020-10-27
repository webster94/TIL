import sys
sys.stdin = open('뿌요뿌요.txt','r')
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def dfs(n):
    q= []
    cnt = 0
    q.append(n)
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6:
                arr[nr][nc] = arr[n][c]




arr = [list(input()) for _ in range(12)]
# 내려 갈 수 있는 지 확인해야하고
# dfs로 4개 이상인지 확인한다.
# 4개 이상이면 .으로 바꾸고 글자들을 아래로 내려갈 수 있는 체크한 후에
# 내리는 함수를 구현해야한다.
#dfs로 4개 인것 부터 확인자
dist = [[0]*6 for _ in range(12)]
for i in range(12):
    for j in range(6):
        if dist[i][j] == 0 and arr[i][j] != '.':
            dfs((i,j))


print(dist)