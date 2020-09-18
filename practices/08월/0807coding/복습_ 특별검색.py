# 선택정렬!!

arr = [64,25,10,22,11]
N = len(arr)
for i in range(0,10):
    idx = i  # 최솟값 찾기 , 시작 위치를 최솟값 가정
    if i %2 ==0:
        for j in range(i+1,N):
            if arr[idx] < arr[j]:
                idx = j
            arr[i],arr[idx] = arr[idx],arr[i]
    else:
        for j in range(i+1,N):
            if arr[idx] > arr[j]:
                idx = j
            arr[i],arr[idx] = arr[idx],arr[i]
print(arr)