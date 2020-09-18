import sys
sys.stdin = open("input.txt","r")
# 직사각형 1은 가로 10 세로 20
# 직사각형 2는 가로 20 세로 20
# 직사각형 3은 가로 20 세로 10
#길이 length를 입력 받는다.
#우선 직사각형1 자르기,
#아니면 직사각형2 자르기,
#아니면 직사각형3 자르기,
#그 후 남은 길이를 재귀 호출 ----> 제한 시간 초과

# 길이가 10인 종이는 1가지
# 길이가 20인 종이는 3가지
# 길이가 30인 종이는 길이가 10,20, 20,10 이렇게 나눈다.
# 길이가 40인 종이는 길이가 20,20, 30,10 이렇게 나눈다.
# 길이가 N인 종이는 N-20,20, N-10, 10 이렇게 나뉜다.
# 이는 작은 부분으로 쪼개서 생각할 수 있으므로
# N-20 일 때는 직사각형 2와 직사각형 3 두가지로 붙일 수 있고
# N-10 일 때는 직사각형 1로 붙일 수 있다.
# 동적계획법을 통해 문제를 접근
dp = [0]*31
dp[1:3] = [1,3] #종이 길이 10일때, 20일때 가지수
for t in range(1,int(input())+1):
    N = int(input())//10
    for i in range(1,N+1):
        if dp[i]==0:
            dp[i] = dp[i-2]*2+dp[i-1]

    print('#{} {}'.format(t,dp[N]))


# def rectangle_cut(length):
#     cut = stack.pop()
#     length-=cut
#
#     if length <= 0:
#         if length == 0:
#             cnt[0]+=1
#     else:
#         for rectangle in rectangles:
#             stack.append(rectangle[0])
#             rectangle_cut(length)
#
# rectangles = [[10,20],[20,10],[20,20]]
#
# for t in range(1,int(input())+1):
#     N = int(input())
#     length = N
#     stack = []
#     cnt = [0]
#     for rectangle in rectangles:
#         stack.append(rectangle[0])
#         rectangle_cut(length)
#
#     print('#{} {}'.format(t,cnt[0]))
