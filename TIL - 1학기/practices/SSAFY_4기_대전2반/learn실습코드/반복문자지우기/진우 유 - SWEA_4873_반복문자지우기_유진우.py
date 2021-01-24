def check(s):
    if len(s) == 1:
        return s
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            tmp = s[:i] + s[i+2:]
            return check(tmp)
    return s

for tc in range(1, int(input())+1):
    text = input()

    print('#{} {}'.format(tc, len(check(text))))