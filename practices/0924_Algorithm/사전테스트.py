import sys
sys.stdin = open("사전.txt","r")

T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    answer = list(map(int,input().split()))
    ans = []
    for i in range(N):
        count = 0
        stud = list(map(int,input().split()))
        result = 0
        for j in range(M):
            if stud[j]==answer[j]:
                count+=1
                result += count
            else:
                count = 0
        ans.append(result)
    print(max(ans)-min(ans))
