arr = [1,2,3]
N = 3

def perm(idx):

    if idx == N:
        print(arr)
        return

    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

perm(0)