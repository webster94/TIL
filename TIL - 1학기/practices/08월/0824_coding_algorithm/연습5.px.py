def euisoo(array,pattern):
    i,j = 0,0
    M = len(array)
    N = len(pattern)
    while (i < M and j < N):
        if array[i] != pattern[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == N:
        return i - N
    else:
        return -1

array = 'eunmookisgoingtostudyhardisname'
pattern = 'mook'
print(euisoo(array,pattern))