# T = int(input())
# for t in range(1,T+1):
#     str1 = input()
#     str2 = input()
#     i,j = 0,0
#     result = 0
#     while i < len(str1) and j < len(str2) and len(str1)<len(str2):
#         if str1[i] != str2[j]:
#             i = -1
#             j = j-i
#         i +=1
#         j +=1
#     if i == len(str1):
#         result = 1
#     else:
#         result = 0
#     print(f'#{t} {result}') 6개정답 4개 오답입니다 ㅠㅠ 정답을 찾을 수 없었습니다 ..
#
T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    if (str2.find(str1)) >0:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')