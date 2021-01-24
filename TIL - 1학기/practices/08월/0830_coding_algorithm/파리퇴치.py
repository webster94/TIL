T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for n in range(M):
                for m in range(M):
                    total += arr[i+n][j+m]
            result.append(total)
    print("#{} {}".format(t,max(result)))