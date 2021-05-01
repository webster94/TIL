def Permutation(depth,idx):
    if depth == M :
        print(' '.join(map(str,arr)))
        return
    for i in range(idx,N):
        arr.append(i+1)
        Permutation(depth+1,i)
        arr.pop()

import sys
N,M = map(int,sys.stdin.readline().split())
arr = []
Permutation(0,0)
