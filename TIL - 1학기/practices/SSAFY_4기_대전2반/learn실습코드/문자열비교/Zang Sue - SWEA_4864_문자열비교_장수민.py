def pattern_match(pattern, text):
    p = len(pattern)
    t = len(text)
    for i in range(t - p + 1):
        cnt = 0
        for j in range(p):
            if text[i + j] == pattern[j]:
                cnt += 1
        if cnt == p:
            return 1
    return 0


for tc in range(1, int(input()) + 1):
    pattern = input()
    text = input()
    result = pattern_match(pattern, text)

    print('#{} {}'.format(tc, result))