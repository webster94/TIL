N = 3
sel = [0] * N
visited = [0] * N
arr = [1,2,3]

def perm(n,idx):
    if n == idx:
        print(sel)
        return
    for i in range(n):
        if visited[i] :
            continue
        sel[idx] = arr[i]
        visited[i] = 1
        perm(n,idx+1)
        visited[i] = 0
perm(N,0)