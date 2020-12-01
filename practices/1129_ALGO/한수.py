def function(n):
    if n[0]-n[1] == n[1]-n[2]:
        return 1
N = int(input())
result = 0
result1= 0
for i in range(1,N+1):
    if i < 100:
        result +=1
    else:
        arr =list(map(int,str(i)))
        if arr[0] -arr[1]== arr[1]-arr[2]:
            result +=1
print(result)

