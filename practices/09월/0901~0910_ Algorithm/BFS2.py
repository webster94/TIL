# BFS의 핵심은 인접리스트를 받는 것이다!
# 인접리스트의 st 에 en값을 넣고
# 인접리스트의 en 에 st값을
# if 넣는다:
#
# 리스트를 다 받았으면 visited를 받고 함수를 호출한다
#
# BFS 함수호출
# q를 생성하고
# 방문체크를 한다
# q값이 0보다 크다면
# 와일문을
# not 돌린다
# t에다가 pop(0)를 저장하고
# for 문을 돌려
#     list_adj의 t에 있는 배열에 방문하지않은 곳이 있다면
#     q에 다가 appenp[i]를 하고
#     방문자에 visited[i]를 1로 넣는다.
# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
def BFS(a):
    visited[a] = 1 #방문체크
    q = []
    q.append(a) #들어가게끔 시킨다.
    while len(q) > 0:
        t = q.pop(0)
        print(t, end = " ")

        for i in list_adj[t]: # 이분이 매우 미숙하네  ㅋㅋ
            if not visited[i]:
                visited[i] = 1
                q.append(i)


V,E  = map(int,input().split())
list_adj = [[] for _ in range(E)]
for i in range(E):
    st,en = map(int,input().split())
    list_adj[st].append(en)
    list_adj[en].append(st)
visited = [0] * (V+1)
BFS(1)

