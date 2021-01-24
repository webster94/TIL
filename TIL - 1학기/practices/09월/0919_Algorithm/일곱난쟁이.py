import sys
sys.stdin = open("일곱난쟁이.txt","r")
def powerset(n,k):
    global numbers
    if n == k:
        total = 0
        numbers = []
        for i in range(n):
            if visited[i] ==1:
                total += arr[i]
                numbers.append(arr[i])
        # print(numbers)
        if total == 100 and len(numbers) == 7:
            numbers.sort()
            return True

    else:
        visited[k] = 1
        if powerset(n,k+1):
            return True
        # powerset(n,k+1)
        visited[k] = 0
        if powerset(n,k+1):
            return True

arr = []
N = 9
for i in range(N):
    arr.append(int(input()))

visited = [0] * N
powerset(N,0)
for j in numbers:
    print(j)

