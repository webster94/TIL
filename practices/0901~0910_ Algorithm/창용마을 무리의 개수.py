# 리스트에 인접하는 마을을 연결하는 것을 만들고, co
import sys
sys.stdin = open("창용마을 무리의 개수.txt","r")

def BFS(n):
    visited[n] = 1
    global cnt
    q = []
    q.append(n)
    cnt +=1
    while len(q) > 0:
        t = q.pop(0)
        for i in list_adj[t]:
            if not visited[i]: # 등록되어있지않다면!
                visited[i] = 1
                q.append(i)




T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    list_adj = [[] for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        st,en = map(int,input().split())
        list_adj[st].append(en)
        list_adj[en].append(st)
        # 입력 받았음
    visited = [0] * (N+1)
    for n in range(1,N+1):
        if visited[n] != 1:
            BFS(n)
    print("#{} {}".format(t,cnt))



