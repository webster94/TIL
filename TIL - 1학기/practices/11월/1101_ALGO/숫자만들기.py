import sys
sys.stdin = open('숫자만들기.txt','r')

def perm(result,p,m,mt,d,i):
    if i == len(arr) :
        ans.append(result)
    if p:
        perm(result + arr[i],p - 1, m , mt, d, i + 1)
    if m:
        perm(result-arr[i],p,m-1,mt,d,i+1)
    if mt:
        perm(result*arr[i],p,m,mt-1,d,i+1)
    if d:
        perm(int(result/arr[i]),p,m,mt,d-1,i+1)
T = int(input())
for t in range(1,T+1):
    N = int(input())
    tools = list(map(int,input().split()))
    p = tools[0]
    m = tools[1]
    mt = tools[2]
    d = tools[3]
    arr = list(map(int,input().split()))
    result = arr[0]
    i = 1
    ans= []
    perm(result,p,m,mt,d,i)

    print('#{} {}'.format(t,max(ans) - min(ans)))



