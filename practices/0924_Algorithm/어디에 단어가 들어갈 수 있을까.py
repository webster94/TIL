import sys
sys.stdin = open("어디단어.txt","r")
T = int(input())
for t in range(1,T+1):
    N,K = map(int,(input().split()))
    bin = [[0] * (N+2) for _ in range(N+2)]
    arr = [list(map(int,input().split())) for _ in range(N)]
    garo = 0
    sero = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            bin[i][j] = arr[i-1][j-1]
    for i in range(len(bin)):
        count = 0
        for j in range(len(bin[0])):
            if bin[i][j] == 1 :
                count +=1
                if count ==K and bin[i][j+1]==0:
                    garo += 1
            else:
                count = 0
        for j in range(len(bin[0])):
            if bin[j][i] == 1 :
                count +=1
                if count ==K and bin[j+1][i]==0:
                    sero += 1
            else:
                count = 0

    print("#{} {}".format(t,garo+sero))