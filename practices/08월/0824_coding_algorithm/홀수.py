# T= int(input())
# for t in range(1,T+1):
#     numbers = list(map(int,input().split()))
#     result = 0
#     for number in numbers:
#         if number % 2 == 1:
#             result += number
#         else:
#             continue
#             result += number
#
#     print(f'#{t} {result}')
    #
    # T = int(input())
    # for t in range(1, T + 1):
    #     numbers = list(map(int, input().split()))
    #     print(f'#{t} {sum((numbers) // len(numbers))}')
    #
    # T = int(input())
    # for t in range(1, T + 1):
    #     a,b = list(map(int, input().split()))
    #     if a > b:
    #         print(f'#{t} >')
    #     elif a < b:
    #         print(f'#{t} <')
    #     else:
    #         print(f'#{t} =')


# T = int(input())
# for t in range(1,T+1):
#     numbers = input()
#     year= numbers[:3]
#     month30 = [4,6,9,11]
#     month31 = [1,3,5,7,8,10,12]
#     month2 = [2]
#     if int(numbers[4:5]) > 12:
#         print(-1)
#         break
#     else:
#         if int(numbers[4:5]) in month30:
#             if int(numbers[6:7]) > 30:
#                 print(-1)
#                 break
#             else:
#                 print(f'#{t} {year} {numbers[4:5]} {numbers[6:7]}')
#
T = int(input())
for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    i = len(numbers)//2
    print(f'#{t} {numbers[i]}')