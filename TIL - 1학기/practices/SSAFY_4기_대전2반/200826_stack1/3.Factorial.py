# #
# def factorial(n):
#     if n == 1:
#         return 1
#
#     return n * factorial(n-1)
#
# print(factorial(5))



def count(N):
    if N==0:
        print("발사아아")
        return
    print(N,"!")
    count(N-1)

count(5)
#
# def 무한호출():
#     무한호출()
#
#
# 무한호출()