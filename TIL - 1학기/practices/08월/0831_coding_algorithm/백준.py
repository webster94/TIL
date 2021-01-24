# A,B = map(int,input().split())
# if A > B :
#     print('>')
# elif A < B :
#     print("<")
# else:
#     print("==")

# score = int(input())
# if 100 >= score >=90:
#     print('A')
# elif 90 > score>=80:
#     print('B')
# elif 80 > score>=70:
#     print('C')
# elif 70 > score>=60:
#     print('D')
# elif 60 > score:
#     print('F')


# N = int(input())
#
# if N % 4 == 0 and N % 100 !=0:
#     print(1)
# elif N % 400 == 0:
#     print(1)
# elif N % 100 != 0:
#     print(0)
# else:
#     print(0)
# a = int(input())
# b = int(input())
# if a>0 and b>0 :
#     print(1)
# elif a<0 and b>0 :
#     print(2)
# elif a<0 and b<0 :
#     print(3)
# elif a>0 and b<0 :
#     print(4)



# M,S = map(int,input().split())
# if 0 <= M <= 24 and 0<= S <= 60:
#     if S < 45:
#         M -= 1
#         if  M < 0:
#             M = 23
#         S = 60 + (S - 45)
#     else:
#         S = S -45
#     print("{} {}".format(M,S))

# N = int(input())
# for i in range(1,10):
#     print("{} * {} = {}".format(N,i,N*i))

# n = int(input())
# total = 0
# for i in range(n+1):
#     total += i
# print(total)


# sys.stdin.readline
# # N = int(input())
# for t in range(N):
#     a,b = map(int,input().split())
#     c = a+b
#     print(c)

# for t in range(1,N+1):
#     a,b = map(int,input().split())
#     c = a+b
#     print('Case #{}: {}'.format(t,c))


# for i in range(1,N+1):
#     print('*' * i +' '*(N-i) )


# A = int(input())
# B = list(map(int,(input())))
# for i in range(len(B)-1,-1,-1):
#     print(B[i]* A)
# result = ''
# for i in B:
#     result += str(i)
# print(A*int(result))


# N,X = map(int,input().split())
# numbers = list(map(int,input().split()))
# for i in numbers:
#     if i < X :
#         print(i,end = " ")
#     else:
#         continue
#         print(i)
