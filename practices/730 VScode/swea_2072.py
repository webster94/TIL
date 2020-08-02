T = int(input())

for number in range(1,T+1):
    result = 0
    numbers = list(map(int, input().split())) ## 10개만 어떻게 갖지?

    for test_case in numbers:
        if test_case %2 == 1:
            result += test_case
    print(f'#{number}  {result}' )
    
