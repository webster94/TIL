import sys
sys.stdin = open("input.txt","r")

for t in range(1,int(input())+1):
    cmp = input()
    txt = input()
    m=len(cmp)
    n=len(txt)
    i=j=cnt=0
    while i<n and j<m:
        if txt[i]!=cmp[j]:
            i=i-j
            j=-1
        i+=1
        j+=1
        if j == m:
            cnt+=1
            j=0

    print('#{} {}'.format(t,cnt))