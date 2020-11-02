import sys
sys.stdin = open('화물도크.txt','r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[1])
    res = 1
    finish = arr[0][1]
    for i in range(1,N):
        if arr[i][0] >= finish:
            res += 1
            finish = arr[i][1]
    print('#{} {}'.format(t,res))



