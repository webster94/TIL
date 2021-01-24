#for t in range(int(input())):print(f'#{t+1}',1 if input()in input() else 0)
def sol(n,h):
    a=len(h);b=len(n);r=[]
    for i in range(a-b+1):
        for j in range(b):
            if n[j]!=h[i+j]:break
        else:r.append(i)
    return 1 if r else 0
for t in range(int(input())):print('#{} {}'.format(t+1,sol(input(),input())))