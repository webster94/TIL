t = int(input())
for c in range(1, t + 1):
    a = input()
    b = input()
    if a in b:
        print(f'#{c} 1')
    else:
        print(f'#{c} 0')