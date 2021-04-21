def start():
    result = []
    for i in range(N-7):
        for j in range(M-7):
            countB = 0  # 고쳐야할 대상
            countW = 0 # 고쳐야할 대상
            for n in range(i,i+8):
                for m in range(j,j+8):
                    if (n + m) %2 ==0 :
                        if arr[n][m]!='W':
                            countB +=1
                        if arr[n][m] != 'B':
                            countW +=1
                    else:
                        if arr[n][m]!='B':
                            countB += 1
                        if arr[n][m] != 'W':
                            countW +=1

            result.append(countB)
            result.append(countW)
    print(result)
    print(min(result))



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
start()
