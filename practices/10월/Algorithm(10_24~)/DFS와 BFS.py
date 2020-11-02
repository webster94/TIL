import sys
sys.stdin = open('bfsdfs.txt','r')

def dfs(n):
    print(n, end = ' ')
    visited[n] = 1
    for i in range(1,N+1):
        if arr[n][i] == 1 and not visited[i]:
            dfs(i)
def bfs(n):
    q = [n]
    visited[n] = 0
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1,N+1):
            if arr[v][i] == 1 and visited[i]:
                q.append(i)
                visited[i] = 0


N,M,V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
print(arr)
for _ in range(M):
    st,ed = map(int,input().split())
    arr[st][ed] = arr[ed][st] = 1
dfs(V)
print()
bfs(V)
