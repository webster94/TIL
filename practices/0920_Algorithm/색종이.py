import sys
sys.stdin = open("색종이.txt","r")
T = int(input())
arr = [[0] * 100 for _ in range(100)]
width = set()
for i in range(T):
    x,y = map(int,input().split())
    # 3,7
    # 15,7
    # 5,2
    rcount = 0
    ccount = 0
    for i in range(x,x+10):
        for j in range(y,y+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count +=1

print(count)





