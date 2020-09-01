T = int(input())
for t in range(1,T+1):
    N = int(input())
    li = [2,3,5,7,11]
    result = ''
    for i in li:
        count = 0
        if N % i ==0:
            while N % i == 0:
                N = N//i
                count += 1
            result += str(count) + ''
        else:
            count = 0
            result += str(count) + ''
    result = ' '.join(result)
    print(f'#{t} {result}')


