def inorder(node,n):
    if node == n:
        return tree[n//2]
    node += 1
    if node != n:
        inorder(tree[node])
        print(node,end = " ")
        inorder(tree[node])


T = int(input())
for t in range(1,T+1):
    N = int(input())
    count = 1
    tree = [0]* N**2
    for i in range(1,N):
        if i :
            tree[i*2] += 1
            tree[i*2 +1] += 2
    print(tree)




    # inorder(1)
    # print(tree)