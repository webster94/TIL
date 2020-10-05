import sys
sys.stdin = open("장훈이의 높은 선반.txt","r")


def powerset(idx,b):
    global ans
    total = 0
    result = []
    if idx == N:
        for i in range(N):
            if sel[i] :
                total += members[i]
        if total >= 0 and total < ans:
            ans = total



    sel[idx] = 1
    powerset(idx+1,b)
    sel[idx] = 0
    powerset(idx+1,b)

T = int(input())
for t in range(1,T+1):
    N,B = map(int,input().split())
    members = list(map(int, input().split()))
    result2 = []
    sel = [0] * N
    ans = 109238002394
    powerset(0,B)
    result2.sort()

    print("#{} {}".format(t,ans))
