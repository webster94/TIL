T = int(input())

for t in range(1,T+1):
    total = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        total += number
    result = total/len(numbers)
    print(f'#{t} {round(result)}')