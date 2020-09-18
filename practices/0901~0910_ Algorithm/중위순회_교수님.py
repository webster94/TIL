# 출력은  1번자리로하자.
import sys
sys.stdin = open("중위순회.txt","r")
def inorder(v):
    if len(arr[v]) >= 3:
        inorder(int(arr[v][2]))
    print(arr[v][1] ,end = "")
    if len(arr[v]) == 4:
        inorder(int(arr[v][3]))

for t in range(1,11):
    N = int(input())
    arr = [[]]
    for i in range(N):
        arr.append(input().split())
    # 입력받았음.

    print("#{}".format(t), end = " ")
    inorder(1)
    print()
