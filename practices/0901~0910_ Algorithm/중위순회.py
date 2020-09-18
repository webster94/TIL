import sys
sys.stdin = open("중위순회.txt","r")
def inOrder(v):
    if v != 0:
        inOrder(tree[v][1])
        print(tree[v][0], end = "")
        inOrder(tree[v][2])

for t in range(1,11):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)]
    for i in range(N):
        arr = input().split()
        tree[int(arr[0])][0] = arr[1]
        if len(arr) ==3:
            tree[int(arr[0])][1] = int(arr[2])
            tree[int(arr[2])][3] = int(arr[0])
        if len(arr) ==4:
            tree[int(arr[0])][1] = int(arr[2])
            tree[int(arr[0])][2] = int(arr[3])
            tree[int(arr[2])][3] = int(arr[0])
            tree[int(arr[3])][3] = int(arr[0])
    print("#{}".format(t),end = "")
    inOrder(1)
    print()