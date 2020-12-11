N  = int(input())
count = 0
for _ in range(N):
    arr = input()
    flag = True
    check = []
    for i in range(len(arr)):
        if arr[i] not in check:
            check.append(arr[i])
        elif arr[i] in check and arr[i] == check[-1]:
            check.append(arr[i])
        elif arr[i] in check and arr[i] != check[-1]:
            flag = False
        else:
            check.add(arr[i])
    if flag:
        count +=1
print(count)





