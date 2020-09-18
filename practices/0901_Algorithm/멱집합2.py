N = 3
arr = [1,2,3]
# 멱집합을 구해보자
# 방문한 곳을 안가기 위해선 방문자리스트가 필요하다. 2차원배열이 아닌 1차원 배열로!
visited = [0] * N
def powerset(n,k):
    if n == k:
        for i in range(n):
            if visited[i] :
                print(arr[i], end = " ")
        print()
    else:
        visited[k] = 1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)