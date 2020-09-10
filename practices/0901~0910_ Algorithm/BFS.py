def BFS(numbers,v): # 함수 호출시에는 numbers를 받는게 맞는가?
    visited = [0] * N
    q = []
    q.append(v) # 시작점을 큐에 삽입
    while len(q) > 0 :
        t= q.pop(0)
        if not visited[t]:
            visited[t] = True
            BFS[G,t] # 방문을 어떻게 해야할지 모르겠꾼
        for i in numbers[t]:
            if not visited[i]:  # 그래프를 어떻게 사용하는가?
                q.append(i)
N,M = map(int,input().split())
for _ in range(M):
    numbers = list(map(input().split()))
    for i in range(M):
        for j in range(M):
            numbers[i][j]=numbers[j][i]=1 # 2차원배열에 입력을 넣는것이 맞는가?
