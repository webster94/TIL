T = int(input())
for t in range(1,T+1):
    li = list(map(int,input().split()))
    big = 0
    sma = li[0]
    for i in range(10):
        if  big <= li[i]:
            big =li[i]
            big_b = i
        if sma >= li[i]:
            sma = li[i]
            sma_s = i
    li[big_b] = 0
    li[sma_s] = 0
    result = round(sum(li) / 8)
    print(f'#{t} {result}')



