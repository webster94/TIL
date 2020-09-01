for t in range(1,11):
    plaza = int(input())
    numbers = list(map(int,input().split()))
    while max(numbers) -min(numbers) > 0 and plaza>0:
        numbers[numbers.index(max(numbers))] -= 1
        numbers[numbers.index(min(numbers))] += 1
        plaza -= 1
    print(f'#{t} {max(numbers)-min(numbers)}')