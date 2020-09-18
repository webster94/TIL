import sys
sys.stdin = open('창용마을.txt','r')

def BFS(n):
    global count
    count +=1
    visit[n] = 1
    q = []
    q.append(n)
    while q:
        t = q.pop(0)
        for k in list_adj[t]:
            if visit[k] == 0:
                q.append(k)
                visit[k] = 1

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    count = 0
    visit = [0] * (N+1)
    list_adj =[[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        list_adj[a].append(b)
        list_adj[b].append(a)
    for i in range(1,N+1):
        if visit[i] == 0:
            BFS(i)
    print(count)