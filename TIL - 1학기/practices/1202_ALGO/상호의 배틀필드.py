import sys
sys.stdin=open('1873.상호의 배틀필드.txt','r')
# 시작지점을 찾는다.
T = int(input())
for t in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    print(arr)
# 문자대로 이동을한다.
# 포탄 발사시와 이동시를 나눠서 구분
