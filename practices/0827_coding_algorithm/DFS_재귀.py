#정점 입력 받자
# 정점 확인 함수
# 방문체크 하고
# visited에다가 1을 저장
# for i in range(1,V+1 정점)

# def DFS(v):
# # 정점을 확이냏야함
# if arr[v][i] == 1 and visited[i] ==0:
#     DFS[i]
# 정점의 수와 간선의 수를입력받는다:
def DFS(v):
    print(v, end= " ")
    visited[v] = 1
    for i in range(1,V+1):#?
        if arr[v][i] == 1 and visited[i] == 0:
            DFS(i)


V,E = map(int,input().split()) # 정점의수와 간선의 수를 입력받아.
# 빈배열 형성
arr= [[0]* (V + 1) for _ in range(V+1)]  # 함수번호 맞춘다? 이해안감
# 행렬입력
for i  in range(E): # (간선의 갯수 만큼)
    st,ed =map(int,input().split())
    arr[st][ed] = arr[ed][st] = 1
# 방문자리 만들자
visited = [0]* (V + 1)
DFS(1)

# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7