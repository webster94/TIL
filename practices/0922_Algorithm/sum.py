import sys
sys.stdin = open("sum.txt","r")
for t in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    sum3 = 0
    sum1= 0
    sum4 = 0
    result = []
    for i in range(100):
        sum1 = sum(arr[i])
        sum2 = 0
        for j in range(100):
            sum2 += arr[j][i]
            if i == j:
                sum3 += arr[i][j]
            elif i == 99-j:
                sum4 += arr[i][j]
        result.append(sum1)
        result.append(sum2)
    result.append(sum3)
    result.append(sum4)
    print("#{} {}".format(t,max(result)))