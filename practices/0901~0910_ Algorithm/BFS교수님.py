#정점수, 간선수
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
# V,E 입력을 받는다.
# 인접리스트 항목을 만든다.
# 시작점과 간선의 수를 받는다.
#   st,en 의 입력받고
# 시작점과 끝점을 인접리스트에 넣는다
#
# visted 리스트를 형성
# 함수를 만든다:
#  q에 빈리스트를 만들고 시작점을 넣는다.
#     시작점 방문체크!!
# 이후 while문을 돌건데 린 q 가 0 클경우, 돌게한다.
# 와일문에선 한개를 하나꺼내고 print 출력을 하고
# for i in 인접리스트를 가져와서 만약에서 그정점을 방문하지않았다면 q에 하나 그 정점을 넣고
#     그 정점을 방문체크한다.
# 따로 재귀호출을 하지않고 무조건 q에 넣는 것이다.
# 너비우선탐색이 완성이되는것이다.
def BFS(a):
    q = []
    visited[a] = 1  # 방문체크
    q.append(a) # 시작점을 방문체크
    while len(q) > 0:
        t = q.pop(0)
        print(t, end = " ")
        for i in list_adj[t]:  #  인접리스트 인덱스에 연결된 1차원 배열 을 수색
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)



N,M = map(int,input().split())
list_adj = [[] for _ in range(N+1)]
for _ in range(M):
    st,en = map(int,input().split())
    list_adj[st].append(en)
    list_adj[en].append(st)
print(list_adj)
visited = [0] * (N+1)
BFS(1)

