for t in range(int(input())):
    p=[]
    for i in input():
        if len(p)==0:p.append(i)
        elif i!=p[-1]:p.append(i)
        else:p.pop()
    print(f'#{t+1}',len(p))