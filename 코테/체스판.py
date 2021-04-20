def startwithW():
    countW = 0
    for i in range(N):
        for j in range(M):
            if i % 2 == 0 and j % 2 == 0:
                if arr[i][j] != 'W':
                    countW +=1
            elif i %2 and j %2 :
                if arr[i][j] != 'W':
                    countW +=1
    return countW
def startwithB():
    countB = 0
    for i in range(N):
        for j in range(M):
            if i % 2 == 0 and j % 2 == 0:
                if arr[i][j] != 'B':
                    countB +=1
            elif i %2 and j %2 :
                if arr[i][j] != 'B':
                    countB +=1
    return countB

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
res1 = startwithW()
res2 = startwithB()
# print(res1,res2)
if res1 > res2 :
    print(res2)
else:
    print(res1)