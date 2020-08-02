alpabet = input()
result = 0
for i in alpabet:
    result = ord(i) - 64
    print(result, end = ' ')