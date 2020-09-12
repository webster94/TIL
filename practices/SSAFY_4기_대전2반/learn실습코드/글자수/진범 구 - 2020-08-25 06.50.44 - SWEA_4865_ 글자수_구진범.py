# for t in range(int(input())):
#     a=input();b=input();r=0
#     for i in a:r=max(r,b.count(i))
#     print('#{} {}'.format(t+1,r))

for t in range(int(input())):
    a=input();b=input();r=0
    for i in range(len(a)):
        cnt=0
        for j in range(len(b)):
            if a[i]==b[j]:cnt+=1
        if r<cnt:r=cnt
    print('#{} {}'.format(t+1,r))