import sys
sys.stdin = open('결혼식.txt','r')

def bfs(n):
    global cnt
    visited[n] = 1
    q= [(n,0)]

    while q:
        v,dist = q.pop(0)
        for i in friends[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                if dist +1 < 2:
                    q.append((i,dist+1))


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    friends = [ [] * (N+1) for _ in range(N+1)]
    visited = [0]* (N+1)
    cnt = 0
    for i in range(M):
        st,en = map(int,input().split())
        friends[en].append(st)
        friends[st].append(en)
    bfs(1)
    print('#{} {}'.format(t,cnt))
