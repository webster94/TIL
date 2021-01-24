# def DFS_Recursive(G,v):
#     if visited[v] = True:
#
#         for each all w in adjacency(G,v):
#             if visited[w] != True:
#                 return DFS_Recursive(G,w)
# ----
# 정점, 간선
# 간선들...

# 인접행렬
# 방문체크

# 간선들을 인접행렬에 저장

def dfs(v):
# 방문체크
    visited[v] = 1
    print(v,end = " ")
    # v의 인접한 정점중에서 방문 안한 정점을 재귀호출
    for w in range(1,N+1):
        if G[v][w]==1 and visited[w] == 0:
            dfs[w]


N,E = map(int,input().split())
# 간선들
temp = list(map(int,input().split()))
#인접행렬
G = [[0]*(N+1) for _ in range(N+1)]
#방문체크
visited = [0] * (N+1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s,e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs()