def dfs(v):
    visited[v] = 1

    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        i, j = map(int, input().split())
        G[i][j] = 1

    s, g = map(int, input().split())
    dfs(s)

    print('#{} {}'.format(tc, visited[g]))