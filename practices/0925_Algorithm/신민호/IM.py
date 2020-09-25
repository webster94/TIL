import sys
sys.stdin = open("IM.txt","r")
T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    signal = list(map(int,input().split()))
    pwd = list(map(int,input().split()))
    td = []
    i = 0
    j = 0
    while len(td) != len(pwd) and i<len(pwd) and j < len(signal):
        if pwd[i] == signal[j]:
            td.append(pwd[i])
            i+=1
            j+=1
        else:
            j+=1

    if len(td) == len(pwd):
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))