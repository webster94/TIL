N = int(input())
arr = []
for i in str(N):
    arr.append(i)
arr.sort(reverse=True)
arr=''.join(arr)
print(arr)