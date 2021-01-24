import sys
sys.stdin = open('숫자만들기.txt','r')
#숫자나열하기.
tools = ['+','-','*','/']
T = int(input())
for t in range(1,T+1):
    N = int(input())
    plus,minus,multi, divis = map(int,input().split())
    arr= list(map(int,input().split()))
    print(arr)

