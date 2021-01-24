def DFS(v):
    work[v] = 1 #노드 방문을 했으니 작업했음을 표시
    for w in adj[v]: # 해당 작업의 후행 작업 순회
        if not work[w]: #해당 작업을 하지 않았으면 수행
            DFS(w)

    stack.append(v) #스택에 v작업담기

for tc in range(1, 11):
    V, E = map(int, input().split())
    #인접리스트
    adj = [[] for _ in range(V+1)]
    work = [0] * (V+1)#일을 했는지 안했는지 쳌
    count = [0] *(V+1)#선행작업 카운트

    stack = []

    edge = list(map(int, input().split()))
    for i in range(0, E):
        st, ed = edge[i*2], edge[i*2+1]
        adj[st].append(ed)
        count[ed] += 1 #선행작업 개수 증가.

    for i in range(1, V+1):
        if count[i] == 0: #선행 작업이 없는 노드 먼저 시작!
            DFS(i)

    print("#{}".format(tc), end =" ")
    print(*stack[::-1])