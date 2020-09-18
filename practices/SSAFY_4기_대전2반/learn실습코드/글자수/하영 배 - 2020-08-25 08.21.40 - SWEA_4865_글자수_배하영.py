T = int(input())
for tc in range(1, T + 1):
    s1 = input()
    s2 = input()
    mydic = {}
    for s in s1:
        if s not in mydic:
            mydic[s] = 0
    for s in s2:
        if s in mydic:
            mydic[s] += 1
    res = sorted(mydic.items(), key=lambda x: x[1], reverse=True)
    print('#{} {}'.format(tc, res[0][1]))