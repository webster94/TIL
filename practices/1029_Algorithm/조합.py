def comb(k,s):
    if k ==R :
        print(bin)
        return
    else:
        for i in range(s,N):
            visited[i] = 1
            bin.append(a[i])
            comb(k+1,s+1)
            visited[i] = 0
            bin.pop()

a = [1,2,3,4,5]
# 5C3?
N = len(a)
R = 3
visited = [0] * N
bin = []
comb(0,0)


