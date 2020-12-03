import sys
sys.stdin = open('그룹나누기.txt','r')

def bfs(n):
    q = [n]
    global cnt
    cnt += 1
    while q:
        v = q.pop(0)
        # print(v)
        for i in group[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    partner = list(map(int,input().split()))
    visited = [0] * (N+1)
    group = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(0,len(partner),2):
        group[partner[i]].append(partner[i+1])
        group[partner[i+1]].append(partner[i])

    for i in range(1,N+1):
        if not visited[i]:
            bfs(i)
    print("#{} {}".format(t, cnt))
    # print(visited)
