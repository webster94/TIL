import sys; sys.stdin = open("input (34).txt","r")


T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    bin = {}
    for i in numbers:
        bin[i] = bin.get(i,0)+1
    tbin=bin.items()
    sbin = sorted(tbin,key=lambda x:x[1],reverse=True)
    print("#{} {}".format(t,sbin[0][0]))
