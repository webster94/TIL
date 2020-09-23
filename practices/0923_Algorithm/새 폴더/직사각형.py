import sys
sys.stdin = open("직사각형.txt","r")
x1,y1,p1,q1,x2,y2,p2,q2  = map(int,input().split())
com1 = []
com2 = []
com1.append(x1)
com2.append(y1)
com1.append(p1)
com2.append(q1)
com1.append(x2)
com2.append(y2)
com1.append(p2)
com2.append(q2)
N = max(com1)
M = max(com2)
arr = [[0] * (N+1) for _ in range(M+1)]
for i in range(y1,q1):
    for j in range(x1,p1):
        arr[i][j] += 1
for i in range(y2,q2):
    for j in range(x2,p2):
        arr[i][j] += 1
if 2 in arr:
    print(True)
else:
    print('d')