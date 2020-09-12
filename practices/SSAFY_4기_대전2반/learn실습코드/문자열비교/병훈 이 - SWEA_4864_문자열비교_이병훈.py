import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    cmp = input()
    txt = input()
    print('#{} 1'.format(t)) if cmp in txt else print('#{} 0'.format(t))
