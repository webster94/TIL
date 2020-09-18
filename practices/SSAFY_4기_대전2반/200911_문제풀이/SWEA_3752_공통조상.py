def search_p(v):
    queue = [v]
    while queue:
        curr = queue.pop(0)

        if tree[curr][2] == 0:
            return

        if tree[curr][2] in parents:
            return tree[curr][2]

        parents.append(tree[curr][2])
        queue.append(tree[curr][2])

def size_tree(v):
    queue = [v]
    count = 0
    while queue:
        curr = queue.pop(0)

        count+=1

        if tree[curr][0]:
            queue.append(tree[curr][0])
        if tree[curr][1]:
            queue.append(tree[curr][1])

    return count

T = int(input())

for tc in range(1,T+1):
    V, E, A, B = map(int,input().split())
    edge = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(V+1)]

    for i in range(E):
        p = edge[i*2]
        c = edge[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    parents=[]

    search_p(A)
    common = search_p(B)
    ans = size_tree(common)

    print("#{} {} {}".format(tc, common, ans))