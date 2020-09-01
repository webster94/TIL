N = 3
arr = [7,8,9]
sel = [0] *3
visited = [0] *3
def euisoo(n,idx):
    if n == idx: # 언제 프린트문 할 것인가
        print(sel)
        return # 리턴 반드시 필요함 아니네..?
    for i in range(N):
        if visited[i]:
            continue
        sel[idx] = arr[i]
        visited[i] = 1
        euisoo(n,idx+1)
        visited[i] = 0
euisoo(N,0)