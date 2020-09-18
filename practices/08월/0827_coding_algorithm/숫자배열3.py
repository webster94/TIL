def rotate(li):
    new = [[0]*N for x in range(N)]
    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = li[i][j]
    return new


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[str(x) for x in input().split()] for _ in range(N)]
    r90 = rotate(arr)
    r180 = rotate(r90)
    r270 = rotate(r180)

    print("#{}".format(t))
    for i in range(N):
        a = ''.join(r90[i])
        b = ''.join(r180[i])
        c = ''.join(r270[i])
        print('{} {} {}'.format(a,b,c))