N = 3
sel = [0] * N
visited = [0] * N
arr = [1,2,3]

def perm(N,idx):
    if N == idx:
        print(sel)
        return
    for i in range(N):
        if not visited[i] :
            sel[idx] = arr[i]
            visited[i] = 1
            perm(N,idx+1)
            visited[i] = 0
perm(N,0)
