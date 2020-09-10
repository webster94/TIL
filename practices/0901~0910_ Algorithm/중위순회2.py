import sys
sys.stdin = open("중위순회.txt","r")

def inOrder(n):
    if len(arr[n]) >= 3:
        inOrder(int(arr[n][2]))
    print(arr[n][1] , end = "")
    if len(arr[n]) ==4:
        inOrder(int(arr[n][3]))


for t in range(1,11) : #
    N = int(input())
    arr = [[]]
    for i in range(N):
        arr.append(input().split()) #이중리스트에 저장한다.
    print("#{}".format(t), end = " ")
    inOrder(1)
    print()

