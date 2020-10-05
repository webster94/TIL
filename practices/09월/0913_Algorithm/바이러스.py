# 인접 리스트를 활용해서 BFS로 풀자
def virus(n):
    global count
    q = []
    q.append(n)
    visit[n] = 1
    while q:
        a = q.pop(0)
        for i in list_adj[a]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
                count +=1




T = int(input())
for t in range(1,T+1):
    N = int(input())
    list_adj = [[] * (N+1) for _ in range(N+1)]
    visit = [0] * (N+1)
    for i in range(N):
        p,c = map(int,input().split())
        list_adj[p].append(c)
    count = 0
    virus(1)
    print(count)
