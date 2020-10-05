import sys
sys.stdin = open("농장.txt","r")
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    x = N//2
    s = x
    e = x
    total = 0
    for i in range(N):
        for j in range(s,e+1):
            total += arr[i][j]
        if i < x:
            s -=1
            e +=1
        else:
            s +=1
            e -=1
    print("#{} {}".format(t,total))