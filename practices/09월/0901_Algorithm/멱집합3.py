#부분집합을 모두 구해보자 powerset을 통해서
N = 3
arr = [1,2,3]
visited = [0] * N

def powerset(n,k):
    if n ==k :
        for i in range(n):
            if visited[i]:
                print(arr[i],end = " ")
        print()
    else:
        visited[k] =1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)