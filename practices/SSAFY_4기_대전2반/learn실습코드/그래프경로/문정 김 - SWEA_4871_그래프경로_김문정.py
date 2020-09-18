# # input 받아서 인접행렬과 방문체크 만들기
# #   인접행렬, 방문체크 만들 시 idx 주의!
# #       node와 일치시키려면 idx값 하나 더 크게!
# # 유향그래프! 인접 행렬 설정할때 a b = b a = 1 하면 안돼.
#
# def check(s,e):
#     visited[s] = 1 # 방문 체크
#     for w in range(1, V+1):
#         if arr[s][w] == 1 and visited[w] == 0:
#             if w == e:
#                 return True
#             else:
#                 check(w, e) # 여기를 return check(w, e)해도 안된다. 왜 return True 하고 빠져나가지 않는걸까?
#
# 입력 코드는 동일
#     if check(S,G):
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))
#

def check(s,e):
    global res
    visited[s] = 1
    for w in range(1, V+1):
        if arr[s][w] == 1 and visited[w] == 0:
            if w == e:
                res = 1 # 왜 res변수에 넣지 않고
                return

            check(w, e)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # input값: 정점수와 간선수
    arr = [[0] * (V+1) for _ in range(V+1)] # 인접 행렬
    for i in range(E): # input값: 행렬에 간선 표시
        a, b = map(int, input().split())
        arr[a][b] = 1 # 유향 그래프!!!!
    visited = [0] * (V+1) # 방문 체크
    S, G = map(int, input().split()) # 경로확인용 출발노드, 도착노드
    res = 0

    check(S,G)

    print('#{} {}'.format(tc, res))
