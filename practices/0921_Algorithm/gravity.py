arr = [7,4,2,0,0,7,0,6,0]
result = 0
maxhight = 0
for i in range(len(arr)):
    # i번째 최대 낙차값은 9 - len(arr) - (i+1)
    maxhight = len(arr) - (i+1)
    for j in range(i+1,len(arr)):
        if arr[i] <= arr[j]
            maxhight -= 1
        #최대값구하기
        if result < maxhight:
            result = maxhight
    print(result)