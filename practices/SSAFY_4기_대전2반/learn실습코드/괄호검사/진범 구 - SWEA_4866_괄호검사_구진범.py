for t in range(int(input())):
    s='{(';f='})';r=1;p=[]
    for i in input():
        if i in s:p.append(i)
        elif i in f:
            if len(p)==0:r=0;break
            elif p.pop()!=s[f.find(i)]:r=0;break
    if len(p):r=0
    print(f'#{t+1}',r)