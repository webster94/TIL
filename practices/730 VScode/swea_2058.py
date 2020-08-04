T = int(input())
for t in range(1,T+1):
    t = list(map(int, input().split()))
    num_max = max(t)
    print(f'#{T} {num_max}')
