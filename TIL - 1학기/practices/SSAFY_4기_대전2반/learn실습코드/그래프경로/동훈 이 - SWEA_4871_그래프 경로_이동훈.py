def DFS(v,e):
    visited[v] = 1
    
    for i in range(1, V + 1):
        if arr[v][i] == 1 and visited[i] == 0:
            DFS(i,e)
    
    if visited[e] == 1:
        return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1

    visited = [0] * (V + 1)
    S, G = map(int, input().split())
    print("#{} {}".format(tc, DFS(S, G)))