# def permutaion():
#    if len(arr) == M:  # 종료 조건!
#        print(' '.join(map(str,arr)))
#        return  # 다시 돌아간다!
#    for i in range(1,N+1):  # 종료가 아닐경우
#        if i in arr:
#            continue
#        arr.append(i)  # arr에 집어 넣고
#        permutaion()  # 다시 순열 돌리고
#        arr.pop() # 다음껄로 넘어가자
# import sys
# N, M = map(int, sys.stdin.readline().split())
# arr = []
# permutaion()
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         for k in range(1, N + 1):
#             for n in range(1, N + 1):
#                 if i != j and j != k and i != k and i != n and n != j and n != k:
#                     print(i, j, k, n)

def permutation():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(1,N+1):
        if i in arr:
            continue
        arr.append(i)
        permutation()
        arr.pop()

N,M = map(int,input().split())
arr= []
permutation()