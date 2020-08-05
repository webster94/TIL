arr = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]
       ]
res = 0
di = [0,0,-1,1]  # y축
dj = [-1,1,0,0]  # x축
N = 5
#탐색
for i in range(N):
    for j in range(N):
        for k in range(4):
            testI=i+di[k] #3
            testJ=j+dj[k]
            if testI>=0 and testI<N and testJ>=0 and testJ <N:
                print(arr[testI][testJ],end = ' ')
            if 0<=testI<5 and 0<=testJ<5:
                res = abs(arr[i][j]-arr[testI][testJ])
print(res)

