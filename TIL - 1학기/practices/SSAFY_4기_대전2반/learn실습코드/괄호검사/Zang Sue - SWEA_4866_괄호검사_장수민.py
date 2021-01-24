import sys
sys.stdin = open("input_check.txt", "r")
def check():
    save = []
    start = ['(', '[', '{']
    end = [')', ']', '}']
    for i in range(len(test)):
        if test[i] in start:
            save.append(test[i])
        for j in range(3):
            if test[i] == end[j]:
                if start[j] not in save:
                    return 0
                else:
                    if save.pop() != start[j]:
                        return 0
    if len(save) != 0:
        return 0
    else:
        return 1
for tc in range(1, int(input()) + 1):
    test = input()
    result = check()
    print('#{} {}'.format(tc, result))