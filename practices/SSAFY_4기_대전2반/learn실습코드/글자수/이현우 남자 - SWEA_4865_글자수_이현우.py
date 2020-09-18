T = int(input())
for tc in range(1, T+1):
    X = input()
    Y = input()
    total = [0]*len(X)
    for i in range(len(X)):
        cnt = 0
        for j in range(len(Y)):
            if X[i] == Y[j]:
                cnt += 1
                total[i] = cnt
    max_number = total[0]
    for k in range(len(total)):
        if max_number < total[k]:
            max_number = total[k]
    print('#{} {}'.format(tc, max_number))