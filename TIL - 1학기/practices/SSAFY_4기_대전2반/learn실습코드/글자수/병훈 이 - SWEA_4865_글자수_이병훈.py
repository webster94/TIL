import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    cmp = set(input())
    txt = input()
    cmp_dict = {}
    for key in cmp:
        cmp_dict[key] = 0

    for char in txt:
        if cmp_dict.get(char)!=None:
            cmp_dict[char]+=1

    print('#{} {}'.format(t,max(cmp_dict.values())))

