import sys
sys.stdin = open('최소합.txt','r')
dr = [ 0, 1 ]
dc = [ 1, 0 ]

def dfs(y,x):
    global result , s
    if result < s :
        return
    if y == N-1 and x == N-1:
        result = s
    for i in range(2):
        nr = y + dr[i]
        nc = x + dc[i]
        if 0 <= nr <N and 0 <= nc < N and (nr,nc) not in visited:
            visited.append((nr,nc))
            s += arr[nr][nc]
            dfs(nr,nc)
            visited.remove((nr,nc))
            s -= arr[nr][nc]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    s, result = arr[0][0], 987654321
    dfs(0, 0)
    print(f'#{tc} {result}')