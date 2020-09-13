import sys
sys.stdin = open("러시아.txt","r")
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input().split()for _ in range(N)]
    print(arr)
