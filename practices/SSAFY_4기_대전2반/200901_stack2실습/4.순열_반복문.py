arr = [1, 2, 3]
for a in range(1, 4):
    for b in range(1, 4):
        if a == b:
            continue
        for c in range(1, 4):
            if a == c or c == b:
                continue
            print(a, b, c)
