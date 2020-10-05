for tc in range(int(input())+1):
    E,N = map(int,input().split())
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)
    # 정점 번호 1~E+1

    arr = list(map(int,input().split()))
    for i in range(0,E*2,2):
        p,c = arr[i], arr[i+1]

        if L[p]:R[p] = c
        else: L[p] = c
        P[c] = p
    ans = 0
    def traverse(v):
        global ans
        if v == 0: return
        ans += 1
        traverse(L[v])
        traverse(R[v])
    traverse(N)
    print(ans)

# # 리턴배열하는 법 !
# # 후위순회를 하는 방법이다.
# for tc in range(int(input()) + 1):
#     E, N = map(int, input().split())
#     L = [0] * (E + 2)
#     R = [0] * (E + 2)
#     P = [0] * (E + 2)
#     # 정점 번호 1~E+1
#
#     arr = list(map(int, input().split()))
#     for i in range(0, E * 2, 2):
#         p, c = arr[i], arr[i + 1]
#
#         if L[p]:
#             R[p] = c
#         else:
#             L[p] = c
#         P[c] = p
#
#
#     def traverse(v):
#         if v == 0: return 0
#         l = traverse(L[v])  결과값머임?
#         r = traverse(R[v])
#         return l+r+1
#
#
#     print(traverse(N))