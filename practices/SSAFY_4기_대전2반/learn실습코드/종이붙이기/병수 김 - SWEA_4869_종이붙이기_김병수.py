
def find(x):
    if x == n:
        return 1
    if x > n:
        return 0
    return find(x+10) + find(x+20)*2


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print('#{} {}'.format(tc, paper(0)))