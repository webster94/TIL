def sol(n):
    if cache[n]==0:cache[n]=sol(n-1)+2*sol(n-2)
    return cache[n]
for t in range(int(input())):cache=[0,1,3]+[0]*298;print(f'#{t+1}',sol(int(input())//10))