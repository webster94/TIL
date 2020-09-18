import sys
sys.stdin = open("input_dfs.txt", "r")

def DFS(s):
    visited[s] = 1
    for i in range(V+1):
        if arr[s][i] == 1 and visited[i] == 0:
            DFS(i)
    return visited
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        arr[x][y] = 1
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    result = DFS(S)[G]
    print('#{} {}'.format(tc, result))
