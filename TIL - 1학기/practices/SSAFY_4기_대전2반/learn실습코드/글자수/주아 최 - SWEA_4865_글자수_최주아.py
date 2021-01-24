import sys
sys.stdin = open("input3.txt", "r")

for T in range(1, int(input()) + 1):
    a = input()
    b = input()

    alphabetList = []

    for i in a:
        alphabetList.append(i)

    alphabetSet = set(alphabetList)
    alphabetList2 = list(alphabetSet)

    number = []

    for i in alphabetList2:
        number2 = b.count(i)
        number.append(number2)

    MAX = max(number)

    print(f'#{T} {MAX}')