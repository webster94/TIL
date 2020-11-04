import sys
sys.stdin = open('N-queen.txt','r')
def nQueen(k):
    global ans
    if k == N:
        for i in range(N-1):
            for j in range(i+1, N):
                if j - i == abs(cols[j] - cols[i]) : return False
        ans +=1
    else:
        for i in range(k,N):
            cols[k], cols[i] = cols[i], cols[k]
            nQueen(k+1)
            cols[k],cols[i] = cols[i] , cols[k]

T= int(input())
for t in range(1,T+1):
    N = int(input())
    cols = [ i for i in range(N)]
    ans = 0

    nQueen(0)
    print("#{} {}".format(t,ans))
