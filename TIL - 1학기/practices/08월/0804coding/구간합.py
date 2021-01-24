T = int(input())
for t in range(1,T+1):
    a,b = list(map(int,(input().split())))
    numbers = list(map(int,(input().split())))
    total = 0
    value = 0
    result = []
    for i in range(0,a-b+1):
        li = numbers[i:i+b]
        total = sum(li)
        result.append(total)
        A = min(result)
        B = max(result)
    value = B-A
    print(f'#{t} {value}')




