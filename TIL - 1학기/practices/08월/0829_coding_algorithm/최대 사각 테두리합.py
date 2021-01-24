# 입력 받고
# for for 에서 처음과 끝값을 이용해서 더한다!
# 최대값을 저장해야겠군

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    # 입력 받았음
    # 이제 더하러 가야지
    result = []
    for i in range(N-K+1):
        for j in range(M-K+1):
            total = 0
            for m in range(K):
                if m == 0 or m == K-1:
                    for n in range(K):
                        total += arr[i+m][j+n]
                else:
                    total += arr[i+m][j]
                    total += arr[i+m][j+K-1]

            result.append(total)
    print("#{} {}".format(t,max(result)))

