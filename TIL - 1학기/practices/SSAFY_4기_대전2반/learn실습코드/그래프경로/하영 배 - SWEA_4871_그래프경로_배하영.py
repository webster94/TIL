T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {}
    visited = []
    res = 0

    for i in range(E):
        fr, to = map(int, input().split())
        if fr in graph:
            graph[fr].append(to)
        else:
            graph[fr] = [to]

    S, G = map(int, input().split())
    st = []
    st.extend(graph[S])
    while len(st):
        x = st.pop()
        if x in visited:
            continue
        else:
            visited.append(x)
        if x == G:
            res = 1
            break
        elif graph.get(x) == None:
            continue
        else:
            st.extend(graph[x])

    print("#{} {}".format(tc, res))