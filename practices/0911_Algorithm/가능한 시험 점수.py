# 모든 부분집합을 구해서 합을 result에 저장시키자. 다음 len(result) 하면 끝이 안나네
# 방문에다가 합을 적어 놓고 포문을 돌려서 result에 합을 저장하면서 나가자
T = int(input())
for t in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    # visit = [[0] * (sum(score) +1) for _ in range(N+1)] # 마지막에 중복을 제거하기위해
    # # 레벨별로
    #
    # def dfs(k,s):
    #     if visit[k][s] : return
    #     visit[k][s] = 1
    #     if k == N: return
    #         # print(s, end = " ")
    #         # visit[s] = 1
    #     else:
    #         dfs(k+1,s) # k번 문제를 틀린경우
    #         dfs(k+1,s+ score[k]) # k번 문제 맞은 경우
    visit = [0] * (sum(score)+1)
    Q = [[0,0]] # k,s
    while Q:
        k,s = Q.pop(0)
        if k == N:
            visit[s] = 1
        else:
            Q.append([k+1,s])
            Q.append([k+1,s+score[k]])
    print(sum(visit))
    # 너비 우선방법임..좋다!

    # print("#{} {}".format(t,sum(visit[N])))
    # Q = [0]
    # for val in score:
    #     for i in range(len(Q)):
    #         if visit[Q[i] + val]: continue
    #         visit[Q[i] + val] = 1
    #         Q.append(Q[i] + val)



