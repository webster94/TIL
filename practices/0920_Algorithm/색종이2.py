import sys
sys.stdin = open("색종이2.txt","r")
N = int(input())
arr = [[0] * 101 for _ in range(101)]
num = 0
result = []
for _ in range(N):
    a,b,ga,se = map(int,input().split())
    num +=1
    for n in range(a,a+ga):
        for m in range(b,b+se):
            arr[n][m] = num
    result.append(num)
bin = {}
for i in arr:
    for j in i:
        if j != 0:
            bin[j] = bin.get(j,0)+1
for i in result:
    if i in bin:
        print(bin[i])
    else:
        print(0)