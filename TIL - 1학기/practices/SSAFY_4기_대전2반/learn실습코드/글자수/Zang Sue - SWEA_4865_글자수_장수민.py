for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    str_dict = {}
    for str in str1:
        str_dict[str] = 0
    for str in str2:
        if str in str_dict:
            str_dict[str] += 1
    result = max(str_dict.values())
    print('#{} {}'.format(tc, result))