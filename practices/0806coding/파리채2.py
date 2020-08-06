T = int(input())
for t in range(1,T+1):
    N,M = list(map(int,input().split()))
    li = [[int(x) for x in input().split()] for _ in range(N)]
    maxfly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for a in range(M):
                for b in range(M):
                    total += li[i+a][j+b]
            if maxfly < total :
                maxfly = total
    print(f'#{t} {maxfly}')