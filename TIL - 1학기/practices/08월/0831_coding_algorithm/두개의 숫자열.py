T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    i = 0
    j = 0
    result = []
    if len(A) > len(B):
        A,B = B,A
    for i in range(len(B)-len(A)+1):
        total = 0
        for j in range(len(A)):
            total += A[j] * B[i+j]
        result.append(total)
    print("#{} {}".format(t,max(result)))
