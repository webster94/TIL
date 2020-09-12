# input
# 정점수, 간선수
# 7 8
# 1 2 #여기부터는 연결되어 있는 두 정점
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

# 입력 먼저
V, E = map(int, input().split())
# 인접행렬 생성 준비
# 한칸더 크게 만드는 이유는 인덱스를 맞추어 주기 위해서
# 0번 인덱스따위 버려버리기
arr = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    st, ed = map(int, input().split())
    # 무향 그래프이기 때문에 서로 연결되있음을 표시
    arr[st][ed] = arr[ed][st] = 1

#방문배열
visited = []
#스택
stack = []
#시작 정점을 담는다.
stack.append(1)

#스택이 빌때까지 무한히 반복
while len(stack) > 0:
    #정점을 하나 꺼낸다.
    v = stack.pop()
    #해당 정점이 방문한 정점이 아니라면
    if v not in visited:
        print(v, end=" ")
        #정점을 방문체크
        visited.append(v)

        #현재 정점에서 연결되어있는 모든 정점을 탐색하기 위한 반복문
        for i in range(1, V+1):
            #현재정점과 연결되어있으면서 방문하지 않은 정점 i가 있다면
            if arr[v][i] == 1 and i not in visited:
                #모두 다 스택에 push
                stack.append(i)
















