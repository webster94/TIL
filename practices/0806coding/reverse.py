T = int(input())
for t in (1,T+1):
    word = input().split()
    # if word == word.reverse()
    if word == word[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
