# 입력 받고
# 빈배열 형성해서
# 처음과 끝을 이용해서 2차원 배열에 1을 담는다.
# # 입력

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    #빈배열 형성
    arr = [[0]*(N+1) for _ in range(N+1)]
    cnt = 0
    bin = {}
    for _ in range(M):
        y1,x1,y2,x2 = map(int,input().split())
        d1 = x2-x1
        d2 = y2-y1
        # arr[x1][y1] = 1
        # arr[x2][y2] = 1

        # 입력은 받았다.
        #이제 해당 배열을 1로 바꿔야한다
        for n in range(N-d2+1):
            for m in range(N-d1+1):
                # if arr[n][m] == 1:
                if n == y1 and m == x1:# 행과열을 조심해야함..ㅎㅎ
                    for a in range(d2+1):
                        for b in range(d1+1):
                            arr[n+a][m+b] = 1
    for i in range(N):
        for j in range(N):
            # if arr[i][j] ==1:
            #     cnt+=1
            bin[arr[i][j]] = bin.get(1,0) +1
    print("#{} {}".format(t,bin[1]))
    # print("#{} {}".format(t,cnt))

