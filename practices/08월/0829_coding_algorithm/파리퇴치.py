# 입력
# arr을 만들고 m크기의 파리채로 찾아서 값을 더한다.
# M*M 에서 더한 최대값을 return 한다.
# 함수를 사용해서 해보좌

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 입력 확인 print(arr)
    max1 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for n in range(M):
                for m in range(M):
                    result += arr[i+n][j+m]
                if max1 <= result:
                    max1 = result
    print("#{} {}".format(t,max1))
        # print("#{}".format(t,max(result)))


