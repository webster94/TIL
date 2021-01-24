import sys; sys.stdin = open()

def DFS(v):
    visit[v] = 1
    if v ==e:
        return 1

    for w in range(1,V+1):
        if G[v][w] == 1 and visit[w] == 0 :
            if DFS(w) ==1:
                return 1
    return 0
# 함수 호출하는 곳에는 모두 리턴을 해야한다.
for tc in range(1,int(input()) + 1):
    V,E = map(int,input().split())
    G = [[0] * V+1 for _ in range(V+1) ]

    for _ in range(E):  #
        u,v = map(int,input().split())
        G[u][v] = 1

    s,e = map(int,input().split())

    visit = [0]*(V+1)

    print(DFS(s))
    # print(visit[e])
