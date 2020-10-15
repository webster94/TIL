import sys
sys.stdin = open('직사각형.txt','r')
arr = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for  j in range(y1,y2):
            arr[i][j] = 1
count = 0
for i in arr:
    for j in i:
        if j == 1:
            count += 1
print(count)