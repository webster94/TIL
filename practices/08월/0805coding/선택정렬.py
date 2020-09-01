def selectionSort(a):
    for i in range(len(a)-1):
        # 최솟값찾기
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min = j
        a[i], a[min] = a[min],a[i]

arr = [64,25,10,22,11]
selectionSort(arr)
print(arr,3)

def selectionSort(a,k):
    for i in range(k):
        # 최솟값찾기
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min = j
        a[i], a[min] = a[min],a[i]
    return a[k-1]