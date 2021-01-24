import sys
sys.stdin = open("줄 세우기.txt","r")
N = int(input())
numbers = list(map(int,input().split()))
main = []
temp = []
for i in range(N):
    student = i+1
    my_back = numbers[i]
    while len(main) > numbers[i]:
        T = main.pop(0)
        temp.append(T)
    temp.append(student)
    while main:
        temp.append(main.pop(0))
    for i in range(len(temp)):
        main.append(temp.pop(0))
for i in range(len(main)):
    print(main[i] , end = " ")