T = int(input())
for t in range(1,T+1):
    count = int(input())
    value = 0
    numbers = list(map(int,input().split()))
    max2 = max(numbers)
    min2 = min(numbers)
    value = max2 - min2
    print(f'#{t} {value}')
    numbers = 0