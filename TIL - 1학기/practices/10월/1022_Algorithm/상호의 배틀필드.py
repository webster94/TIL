import sys
sys.stdin = open('상호의 배틀필드.txt','r')
T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    arr = []
    for _ in range(H):
        arr.append(list(input()))
    number = int(input())
    moves = list(input())
    