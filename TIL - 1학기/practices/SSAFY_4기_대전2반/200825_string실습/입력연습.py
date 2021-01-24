#한줄을 통으로 읽어온다.
#ABCDEF
# line = list(input())
#['A','B','C',.....]

#A B C D E
#스플릿은 공백으로 쪼개는게 기본
# line = input().split()
# ['A', 'B', 'C', 'D', 'E']


#행과 열 그리고 배열정보
# 2 4
# 1 2 3 4
# 5 6 7 8

#2차원리스트 입력
# R , C = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(R)]
#
# for a in arr:
#     print(a)

#1234
# line = list(map(int,list(input())))
#
# print(line)
line = list(map(int, input()))
print(line)

# 3
# XYPV
# EOGGXYPVSY
# STJJ
# HOFSTJPVPP
# ZYJZXZTIBSDG
# TTXGZYJZXZTIBSDGWQLW

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(str1)
    print(str2)