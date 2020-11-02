# def partition(numebers,p,r):
#     x = numbers[r]
#     i = p - 1
#
#     for j in range(len(numbers) - 1):
#         if numbers[j] <= x:
#             i += 1
#             numbers[i] , numbers[j] = numbers[j], numbers[i]
#     numbers[i+1], numbers[r] = numbers[r], numbers[i+1]
#     return i + 1 # 이부분을 잘모르겟어용
def partition(A,l,r):
    p = (l+r) // 2
    i = l+1
    j = r
    while i <= j:
        while(i <= j and A[i] <= A[p]) : i+=1
        while(i <= j and A[i] >= A[p]) : j-=1
        if i<=j:
            if i == p:
                p = j
            A[i],A[j] = A[j],A[i]
        A[l],A[j] = A[j],A[l]
        return j

def quickSort(A,l,r):
    if l < r:
        s = partition(A,l,r)
        if s == N // 2 :
            return
        elif s >  N//2:
            quickSort(A,l,s-1)
        else:
            quickSort(A,s+1,r)
N = int(input())
A = list(map(int,input().split()))
r = len(A) - 1
l = 0
print(partition(A,l,r))
print(A)
#
# 6
# 11 45 23 81 28 34