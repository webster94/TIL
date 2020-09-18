def dfs(x):
    visited[x] = 1
    result.append(x)
    global G
    for w in range(1, V+1):
        if arr[x][w] == 1 and visited[w] == 0:
            dfs(w)
    if G in result:
        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    #인접행렬
    arr = [[0]*(V+1) for _ in range(V+1)]
    #방문체크
    visited = [0] *(V+1)
    # 간선들 인접행렬 저장
    for i in range(E):
        s, e = map(int, input().split())
        arr[s][e] = 1

    # 만날 애들
    S, G = map(int, input().split())

    # 거쳐간 리스트
    result = []

    print('#{} {}'.format(tc, dfs(S)))