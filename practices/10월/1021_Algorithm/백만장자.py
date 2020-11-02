import sys
sys.stdin = open('백만장자.txt','r')

T= int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sell = arr[N-1]
    ans = 0
    for i in range(N-2,-1,-1):
        if sell >= arr[i]:
            ans += sell - arr[i]
        else:
            sell = arr[i]
    print('#{} {} '.format(t,ans))
