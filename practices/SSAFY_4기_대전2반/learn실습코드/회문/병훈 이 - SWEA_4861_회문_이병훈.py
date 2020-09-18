import sys
sys.stdin = open("input.txt","r")
def is_palindrome(txt):
    for i in range(len(txt)//2-1):
        if txt[i]!=txt[len(txt)-1-i]:
            return False
    else:
        return True

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    txts = []
    for i in range(N):
        txts.append(input())
    for i in range(N):
        for j in range(N-M+1):
            row = ''
            col = ''
            for k in range(M):
                row+=txts[i][j+k]
                col+=txts[j+k][i]
        if is_palindrome(row):
            print('#{} {}'.format(t,row))
        if is_palindrome(col):
            print('#{} {}'.format(t,col))


