N =5
sel = [0] * N
visited = [0] * N
arr = [1,2,3,4,5]

def perm(n,idx):
    if N == idx:
        print(sel)
        return
    for i in range(n):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1
            perm(n,idx+1)
            visited[i] = 0
perm(N,0)