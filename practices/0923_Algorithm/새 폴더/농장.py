import sys
sys.stdin = open("농장.txt","r")
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    x = N//2
    total = 0
    for i in range(N):
        if i <= x:
            for j in range(x-i,x+i+1):
                total +=arr[i][j]
        elif i > x:
            for j in range(i-x,N-(i-x)):
                total += arr[i][j]
    print("#{} {}".format(t,total))