# 한줄을 읽어서 정수로 변환
# input() : 한줄을 읽어옴
# int() 정수로 변환
# N = int(input())
# print(N,type(N))
# 한줄을 읽어서 공백으로 구분된 문자를 입력받기.
#input.split("") : 한줄 읽고 구분문자로 나눠서 문자로 이뤄진 리스트 반환
# print(input().split())
# 한줄을 읽고 공백으로 구분된 문자 -> 개수가 정해져 있음
# 1 2
#map(형식.데이터) : 리스트에 있는 데이터를 형식에 맞춰 변환
n,m = map(int,input().split())
print(n,m)
print(type(n),type(m))n,m = input().split()
print(n,m)
print(type(n),type(m))

# 파이썬 복사 control -d
# 시프트+알트+방향키는 위아래 움직일 수 있어.
