import sys
sys.stdin = open("dfs와bfs.txt",'r')
def dfs(v):
    print(v, end = ' ')
    visited[v] = 1
    for i in range(1,N+1):
        if visited[i] == 0 and arr[v][i]==1:
            dfs(i)
def bfs(v):
    q.append(v)
    visited[v] = 0
    while q:
        V = q.pop(0)
        print(V,end = ' ')
        for i in range(1,N+1):
            if(visited[i] ==1) and arr[V][i] ==1:
                q.append(i)
                visited[i] = 0


N,M,V = map(int,input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    st,ed = map(int,input().split())
    #무향이기때문에
    arr[st][ed] = arr[ed][st] = 1
    visited = [0] * (N+1)
    q = []
dfs(V)
print()
bfs(V)