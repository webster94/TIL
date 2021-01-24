N = 3
arr= [4,5,6]
visited = [0] * N
def powerset(n,k):
    if n == k :
        for i in range(n):
            if visited[i] :
                print(arr[i],end = " ")
        print()
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)