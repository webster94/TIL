# try :
#     while True:
#         a,b = map(int,input().split())
#         print(a+b)
# except:
#     exit()
#


number = int(input())
result = 0
result2 = 0
cnt = 0
while result != number:
    cnt += 1
    if number < 10:
        result = number * 10

    for i in str(number):
        result2 += int(i)
    if result2 < 10:
        result2 = result%10 + result2%10
    elif result2 >= 10:
        result = result2
    print(result)
print(cnt)
#
#
#

#
# number = int(input())
# count = 0
# result = 0
# result2 = result//10
# while result != number:
#     result = result +1
#     if result //10 ==3 or result // 10 == 6 or result // 10 == 9:
#         count +=1
#     if result % 10 ==3 or result % 10 == 6 or result % 10 == 9:
#         count +=1
#     if count == 0:
#         print(result , end= " ")
#     else:
#         print('-'*count, end = " ")
#     count = 0
# # 별-9 문제
# T = int(input())
# N = 2*T-1
# i = 0
# for i in range(N):
#     if i <= N//2:
#         print(i*" " + "*"*(N-2*i)+ i*" ")
#     else:
#         print((N-i-1)* " " + "*" * (N-2*N+2*i+2) )


# #별-21
# N  = int(input())
# result1 = ''
# result2 = ''
# for i in range(N):
#     if i%2 == 0:
#         result1 += "*"
#         result2 += " "
#     else:
#         result1 += " "
#         result2 += "*"
# for j in range(N):
#     print(result1)
#     print(result2)

# 최대/최소
# N = int(input())
# numbers = list(map(int,input().split()))
# print(min(numbers), max(numbers))

# # 최댓값
# numbers = [int(input()) for _ in range(9)]
# print(max(numbers))
# print(numbers.index(max(numbers))+1)

# # 숫자의 개수
# numbers = [int(input()) for _ in range(3)]
# total = numbers[0] * numbers[1] * numbers[2]
# result = 0
# for i in range(10):
#     if str(i) in str(total):
#         result = str(total).count(str(i))
#         print(result)
#     else:
#         print(0)
# numbers = [int(input()) for _ in range(10)]
# result = set()
# for i in numbers:
#     result.add(i%42)
# print(len(result))

#평균
# N = int(input())
# numbers = list(map(int,input().split()))
# number = max(numbers)
# change = 0
# total = 0
# for i in numbers:
#     change = i / number* 100
#     total += change
# print(total/N)

# OX퀴즈

# N = int(input())
# for _ in range(N):
#     OX = input()
#     count = 0
#     total = 0
#     for i in OX:
#         if i == 'O':
#             count +=1
#             total += count
#         else:
#             count = 0
#     print(total)
# 평균은 넘겠지.

# C= int(input())
# for _ in range(C):
#     average = 0
#     result = 0
#     people = 0
#     numbers = list(map(int,input().split()))
#     N = numbers[0]
#     numbers.pop(0)
#     average = sum(numbers)/N
#     for i in numbers:
#         if i > average:
#             people +=1
#     print("{}%".format("%0.3f" %(people/N * 100)))
