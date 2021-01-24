import sys
sys.stdin = open('덤프트력.txt','r')
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    W =  list(map(int,input().split()))
    T = list(map(int,input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    i,j = 0, 0
    ans = 0
    while i < N  and j < M :
        if W[i] <= T[j]:
            ans += W[i]
            i += 1
            j += 1

        else:
            i +=1
    print('#{} {}'.format(t,ans))