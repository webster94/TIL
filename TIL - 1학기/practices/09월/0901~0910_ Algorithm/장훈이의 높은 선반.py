def powerset(idx, b):
    global result2
    total = 0
    result = []
    if idx == N:
        for i in range(N):
            if sel[i]:
                total += members[i]
        result.append(total)
        for i in result:
            ans = i - b
            if ans >= 0:
                result2.append(ans)

        return

    sel[idx] = 1
    powerset(idx + 1, b)
    sel[idx] = 0
    powerset(idx + 1, b)


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    members = list(map(int, input().split()))
    result2 = []
    sel = [0] * N
    powerset(0, B)
    result2.sort()

    print("#{} {}".format(t, result2[0]))

