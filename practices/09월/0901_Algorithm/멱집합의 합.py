N = 10
arr = [1,2,3,4,5,6,7,8,9,10]
visited = [0] * N
total = 0
def powerset(n,k):
    if n == k :
        total = 0
        for i in range(N):
            if visited[i] :
                total += arr[i]
        if total == 10:
            print(visited)
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)