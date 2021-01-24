T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 입력받음
    # 이제 들어가아지
    result = 0 #결과값을 넣을 곳
    for i in range(N-M+1): # 전체 행을 확인하고
        for j in range(N-M+1): # 이제 M 범위를 제외하고 모두 돌수 있게!
            total = 0
            for n in range(M): #가로 세로 확인
                for m in range(M):
                    total += (arr[i+n][j+m])
                    if result < total:
                        result = total
            # result.append(total)/
    print("#{} {}".format(t,result))
