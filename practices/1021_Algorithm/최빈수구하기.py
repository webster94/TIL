import sys
sys.stdin = open('최빈수.txt','r')

T= int(input())
for t in range(1,T+1):
    td = int(input())
    arr = list(map(int,input().split()))
    bin = {}
    for i in arr:
        bin[i] = bin.get(i,0)+1
    valuemax = max(bin.values())
    keymax = 0
    for key,value in bin.items():
        if value == valuemax:
            keymax = key
    print('#{} {}' .format(t,keymax))


