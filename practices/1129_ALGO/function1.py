def selfnumber(n):
    return n + sum([int(i) for i in str(n)])

arr = [0] * 10001
for i in range(10000):
    if selfnumber(i) <=10000:
        arr[selfnumber(i)] = 1
for i in range(10000):
    if arr[i]==0:
        print(i)

