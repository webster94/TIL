# def preOrder(index):
#     print(tree[index], end = " ")
#     if tree[index*2] != 0:
#         preOrder(index*2)
#     if tree[index*2 +1] != 0:
#         preOrder(index*2 +1)
def preorder(node):
    global count
    if node:
        count += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

for t in range(1,int(input())+1):
    E,N = map(int,input().split())
    arr= list(map(int,input().split()))
    tree = [[0]*2 for _ in range(len(arr))]
    count = 0
    for i in range(E):
        p,c = arr[i*2], arr[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    preorder(N)
    print("#{} {}".format(t,count))