import sys
sys.stdin = open("input.txt","r")
def check_double():
    for i in range(len(txt)-1):
        if txt[i]==txt[i+1]:return i
    else:return -1

for t in range(1,int(input())+1):
    txt = list(input())
    i = check_double()
    while i!=-1:
        txt.pop(i)
        txt.pop(i)
        i = check_double()
    print('#{} {}'.format(t,len(txt)))
