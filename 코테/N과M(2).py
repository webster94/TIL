def Permutation(s):
    if s == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(s,N):
        if visited[i] : continue
        visited[i] = 1 # 방문 체크
        arr.append(i+1) # arr 에 다음 숫자 추가
        Permutation(s+1) # 깊게 들어가서 다시 순열
        arr.pop() # 끝에껏은  썻으니 제거
        for j in range(i+1,N):
            visited[j] = 0 # false로 지정..

N,M = map(int,input().split())
arr = []
visited = [0] * N
Permutation(0)

## 꼭 다시 풀어보자!!!!