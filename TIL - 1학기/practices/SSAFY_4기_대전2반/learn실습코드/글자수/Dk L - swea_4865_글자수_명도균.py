for test_case in range(1, int(input()) + 1):
    N = input()
    M = input()
    word = {}
    for n in N:
        word[n] = M.count(n)
    result = max(list(word.values()))
    print(f'#{test_case} {result}')