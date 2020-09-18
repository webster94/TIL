

import sys
sys.stdin = open("sample_input.txt", "r")

# 시작점 = S, 종점 = E ( 입력값 마지막에 주어짐)
# S부터 출발해서 E까지 갈 때 경로가 있으면 1 출력, 없으면 0 출력




def route_check(S):
    # 방문체크
    visited[S] = True
    print(S, end, end=" ")
    for w in range(1, V+1):
        if M[S][w] == 1 and visited[w] == 0:
            route_check(w)


T = int(input())
for tc in range(1, T+1):
    # 노드, 간선 입력받기 - 일방향이라서 하나만 입력해도 된다.
    V, E = map(int,input().split())
    # 간선들
    route = list(map(int, input().split()))

    # 인접행렬
    M = [[0] * (V+1) for _ in range(V+1)]

    # 방문 체크 위한 빈 행렬 만들어 주기
    visited = [0] * (V+1)

    for i in range(E):
        depart,arrive = route[2*i], route[2*i+1]
        M[depart][arrive] = 1
        M[arrive][depart] = 1

    print("#{} {}".format(tc, route_check(S)))

# 출발 노드인 S 기준으로 함수를 호출해야 하는데 ..
route_check(S)