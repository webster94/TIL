T = int(input())
for t in range(1,T+1):
    test = input().split()
    numbers =input().split()
    lists = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = ''
    for list in lists:
        for number in numbers:
            if list == number:
               result += number +' '
    print(f'#{t} {result}')