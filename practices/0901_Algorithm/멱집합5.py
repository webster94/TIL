arr = [8,3,2]
N = 3
visited = [0] * N
def powerset(n,k):
    if n == k :
        for i in range(n):
            if visited[i]:
                print(arr[i],end = " ")
        print()
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)