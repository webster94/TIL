 # N*N 배열 안에 있는 N*N 배열의 합이 가장
 # 큰 부분 을 찾는 문제!
 # 필요한 것은
 # 총합을 구할 M*M의 상자
T = int(input())
for t in range(1,T+1):
    N,M = list(map(int,input().split()))
    flys = [[int(x) for x in list(map(int,input().split()))] for _ in range(N)] # 대입완료
    maxfly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            totalfly = 0
            for a in range(M):
                for b in range(M):
                    totalfly += flys[i+a][j+b]
                if maxfly < totalfly:
                    maxfly = totalfly
    print(f'#{t} {maxfly}')