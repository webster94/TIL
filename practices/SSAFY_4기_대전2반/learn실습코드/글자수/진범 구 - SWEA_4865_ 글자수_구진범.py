for t in range(int(input())):
    a=input();b=input();r=0
    for i in a:r=max(r,b.count(i))
    print(f'#{t+1}',r)