def DFS(v):
    visited[v] =1
    #방문체크
    #종료조건!!
    if v==G:
        return 1

    for w in range(1,V+1):
        if arr[v][w] ==1 and visited[w] ==0:
            if DFS(w) == 1:
                return 1 # 종료조건
    return 0


T = int(input())
for t in range(1,T+1):
    V,E = map(int,input().split())
    arr= [[0] * (V +1) for _ in range(V+1)]
    # print(arr)
    visited = [0] * (V+1)
    # print(visited)
    for i in range(E):
        a,b = map(int, input().split())
        arr[a][b] =1  # 등록

    S,G = map(int,input().split())
    print("#{} {}".format(t,DFS(S)))