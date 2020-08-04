T = int(input())
for t in range(1,T+1):
    
    a,b = map(int, input().split())
    result = ''
    if a>b:
        result = '>'
    elif a==b:
        result = '='
    else:
        result = '<'
    print(f'#{t} {result}')


