N = int(input())
for t in range(N):
    arr= input()
    temp = []
    i = 0
    count = 0
    flag = False
    while i < len(arr):
        temp.append(arr[i])
        if len(temp) > 1 and temp[i-1] != arr[i] and arr[i] not in temp:
            flag = False
        elif len(temp) > 1 and temp[i-1] == arr[i] :
            flag = False
        if len(temp) > 1 and temp[i-1] != arr[i] and arr[i] in temp:
            flag = True
            break
        i +=1
    if flag == True:
        count +=1
print(count)