import sys
sys.stdin = open('퀵정렬.txt','r')

def quicksort(A,l,r):
    if l < r:
        s = partition(A,l,r)
        # print(arr)
        quicksort(A,l,s-1)
        quicksort(A,s+1,r)
def partition(A,l,r):
    p = A[l]
    # print(p)
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p  : i += 1
        while i <= j and A[j] >= p : j -= 1
        if i < j :
            if i  == p:
                p = r
            A[i],A[j] = A[j],A[i]
    A[l],A[j] = A[j],A[l]
    return j

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quicksort(arr,0,N-1)
    print(arr)
    print('#{} {}'.format(t, arr[N // 2]))