# def hanoi(n,start,end) :
#     if n == 1 :
#         print(start,end)
#         return
#     else:
#         hanoi(n-1,start,6-(start+end))
#         print(start,end)
#         hanoi(n-1,6-(start+end),end)
#
# N = int(input())
# print(2**N-1)
# hanoi(N,1,3)


# 1단계 : 가장 높이있는 원판을 다른 판으로 옮긴다.
# 2 단계 : 가장 아래 판을 3번쨰 판으로 옮긴다.
# 3 단계 남은 n-1 판을 세번쨰 판으로 옮긴다.
#
# def Hanoi(n,start,end):
#     if n ==1 :
#         print(start,end)
#     else:
#         other = 6-start-end
#         Hanoi(n-1,start,other)
#         print(start,end)
#         Hanoi(n-1,other,end)
#
# N = int(input())
# print(2 **N -1 )
# Hanoi(N,1,3)

def Hanoi(n,start,end):
    #종료조건
    if n == 1:
        print(start,end)
        return
    else:
        other = 6 - start - end
        Hanoi(n-1,start,other)
        print(start,end)
        Hanoi(n-1,other,end)

N = int(input())
print(2**N -1)
Hanoi(N,1,3)


