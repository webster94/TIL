# 망한 보이어무어 코
# T = int(input())
# for tc in range(1, T+1):
#     A = list(",".join(input()).split(","))
#     B = list(",".join(input()).split(","))

#     skip_list = []
#     for num in range(len(A)-1,0,-1):
#         skip_list += [num]
    
#     i = len(A) - 1
#     j = len(B) - 1
#     ans = 0
#     while i <= j:
#         if A[len(A)-1] == B[i]:
#             if B[i-len(A)+1:i+1] == A:
#                 ans = 1
#                 break
#             else:
#                 i += len(A)
#         else:
#             if B[i] in A:
#                 i += skip_list[A.index(B[i])]
#             else:
#                 i += len(A)
    
#     print("#{} {}".format(tc, ans))


def brute(a, b):
    i = 0
    j = 0
    while j < len(a) and i < len(b):
        if b[i] != a[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(a):
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    A = input()
    B = input()

print("#{} {}".format(tc, brute(A, B)))
