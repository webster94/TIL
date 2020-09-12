T = int(input())
for t in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    visit = [[0] * (sum(score) +1) for _ in range(N+1)] # 마지막에 중복을 제거하기위해
    print(visit)
    # 레벨별로


    def dfs(k,s):
        if visit[k][s] : return
        visit[k][s] = 1
        print(visit)
        if k == N: return
            # print(s, end = " ")
            # visit[s] = 1
        else:
             dfs(k+1,s) # k번 문제를 틀린경우
             dfs(k+1,s+ score[k]) # k번 문제 맞은 경우

    dfs(0, 0)
    # print("#{} {}".format(t, sum(visit[N])))
