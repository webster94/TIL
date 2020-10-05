
for t in range(1,int(input())+1 ):
    N = int(input())
    arr = list(map(int,input().split()))

    H = [0] * (N+1)
    hsize = 0
    for val in arr:

        hsize +=1
        H[hsize] = val

        c = hsize
        p = hsize // 2
        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
    ans = 0
    v = N//2
    while v:
        ans += H[v]
        v = v // 2
    print(ans)