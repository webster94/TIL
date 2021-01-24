for c in range(1, int(input()) + 1):
    a = {i:0 for i in input()}
    b = input()
    for k in a.keys():
        a[k] = b.count(k)
    m = max(list(a.values()))
    print(f'#{c} {m}')