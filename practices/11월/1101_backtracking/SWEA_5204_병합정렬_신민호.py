import sys
sys.stdin = open('병합정렬.txt','r')
def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left,right):
    global result ,cnt
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0 :
        result.extend(left)
        cnt += 1
    if len(right) > 0:
        result.extend(right)
    return result

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    result = merge_sort(arr)
    print("#{} {} {}".format(t,result[N//2],cnt))