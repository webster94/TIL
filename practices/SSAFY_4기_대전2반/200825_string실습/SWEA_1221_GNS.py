num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())

for tc in range(1, T + 1):
    a, b = input().split()

    arr = list(input().split())

    cnt = [0] * 10

    for key in arr:
        cnt[num_dict[key]] += 1

    print("#{}".format(tc))

    for i in range(10):
        print(num_list[i] * cnt[i], end="")
    print()
