# import sys
#
# N = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))
# arr2 = set(arr)
# arr2 = sorted(arr2)
#
# dic = {arr2[i]: i for i in range(len(arr2))}
# for i in arr:
#     print(dic[i], end= ' ')

import sys
# N = int(input())
# arr = list(map(int,input().split()))
# arr2= set(arr)
# arr2 = sorted(arr2) # 함수는 안되러라
# dic = {arr2[i]: i for i in range(len(arr2))}  #  사전에 오름차순으로 몇번째인지 등록해준다!!
# for i in arr: # 사전에 등록된 값들이 몇번째인지 나타내주는 포문
#     print(dic[i], end= ' ')


N = int(input())
arr = list(map(int,input().split()))
arr2 = set(arr)
arr2 = sorted(arr2)
dic = { arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end= ' ')