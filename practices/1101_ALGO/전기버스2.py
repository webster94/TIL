import sys
sys.stdin = open('전기버스.txt','r')

def backtraking(a,b,ch,cnt):
    global result

    if a > b:
        return

    if a+ch >= b:
        # print(a,ch,b,cnt)
        result = cnt
        return
    maxi = 0
    j= 0
    for i in range(a + arr[a]+1):
        if maxi <= arr[i]:
            maxi = arr[i]
            j= i # 최대 점프 할 수 있는 인덱스  j
    print('요기')
    print(j)
    backtraking(a+j,b,maxi,cnt+1)

T = int(input())
for t in range(1,T+1):
    arr = list(map(int,input().split()))

    N = arr.pop(0)
    while len(arr) < N:
        arr.append(0)
    cnt = 0
    st = arr[0]
    en = N
    result = 0
    backtraking(1,en,st,cnt)
    print('#{} {}'.format(t,result))
