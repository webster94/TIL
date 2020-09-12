def c(l,n,m):
    for i in l:
        for j in range(n+1-m):
            if i[j:j+m]==i[j:j+m][::-1]:return i[j:j+m]
for t in range(int(input())):n,m=map(int,input().split());l=[input()for _ in range(n)];l+=list(zip(*l));print('#{} {}'.format(t+1,''.join(c(l,n,m))))