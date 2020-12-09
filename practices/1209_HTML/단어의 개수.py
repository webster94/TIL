arr = input()
arr=arr.lstrip()
arr=arr.rstrip()
i = 0
N = len(arr)
count = 1
if N == 0 and arr == '':
    print(0)
else:
    while i < N:
        if arr[i] == ' ':
            count +=1
        i+=1
    print(count)