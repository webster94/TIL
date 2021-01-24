arr = [1,2,3,4,5,6,7]
N = 7
visited = [0] * N
def powerset(n,k):
    if n == k :
        for i in range(k):
            if visited[i] :
                print(arr[i],end = " ")
        print()
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)