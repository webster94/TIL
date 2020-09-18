for tc in range(1,int(input())+1):
    N,M,L = map(int,input().split())
    T = [0] * ( N + 1 )
    for _ in range(M):
        num,val = map(int,input().split())
        T[num] = val # 단말노드를 채워놓음
    # 구할 수 있따.
    for i in range(N-M, 0 , -1):
        T[i] = T[i*2]
        if i*2 +1 <= N:
            T[i] += T[i*2 +1 ]
    dfs(1)
    print(T[L])

    def dfs(v):
        if v > N : return 0
        l = dfs(v*2)
        r = dfs(v*2 +1)
        T[v] += l+r
        return T[v]
