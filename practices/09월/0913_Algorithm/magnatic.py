import sys
sys.stdin = open("마그네틱.txt","r")

for t in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        flag = False
        for j in range(N):
            if arr[j][i] == 1:
                flag = True
            elif arr[j][i] == 2 and flag == True:
                flag = False
                count +=1
    print("#{} {}".format(t,count))
