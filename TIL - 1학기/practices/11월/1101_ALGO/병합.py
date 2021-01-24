def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    global  cnt
    result = [0] * (len(left) + len(right))
    l_i = r_i = i = 0
    if left[len(left)-1] > right[len(right)-1]:
        cnt +=1
    while l_i < len(left) and r_i < len(right):
        if left[l_i] < right[r_i]:
            result[i] = left[l_i]
            l_i += 1
            i += 1
        else:
            result[i] = right[r_i]
            r_i += 1
            i += 1

    while l_i < len(left):
        result[i] = left[l_i]
        l_i += 1
        i += 1
    while r_i < len(right):
        result[i] = right[r_i]
        r_i += 1
        i += 1

    return result


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # result = [0] * (len(arr))
    cnt = 0
    result2 = merge_sort(arr)
    print(result2)
    print("#{} {} {}".format(t, result2[N // 2], cnt))