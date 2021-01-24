T = int(input())
for t in range(1,T+1):
    n = int(input())
    result = []
    numbers = list(map(int,input().split()))
    numbers = sorted(numbers)
    for i in range(0,5):  # 5번 하려고
        result.append(numbers[len(numbers)-i-1])
        result.append(numbers[i])#  처음에 10 이 포함이 되지않아서!! # -1 을 해야줘야한다
    bin = ''
    for k in result:
        bin += str(k) + ' '
    print(f'#{t} {bin}')

