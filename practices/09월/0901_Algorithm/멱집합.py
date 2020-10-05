N =4
A = [1,2,3,4]
visited =  [0] * N

def powerset(n,k):
    if n == k:
        for i in range(n):
            if visited[i] :
                print(A[i],end = " ")
        print()
# 종료조건 모르겠네

    else: # 방문체크를 통해 호출할 것과 안할 것을 구분
        visited[k] =1
        powerset(n,k+1)
        visited[k] = 0
        powerset(n,k+1)
powerset(N,0)

