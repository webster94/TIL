T = int(input())
for t in range(1,T+1):
    str1 = list(input())
    str1_1 = set()
    for i in str1:
        str1_1.add(i)
    # 패턴은 string
    str2 =input()
    # 문장은 리스트
    bin = {}
    count = 0
    for i in str1_1:
        for j in str2:
            if i == j:
                #중복된 수를 막아야해. 그 방법은..
                bin[i] = bin.get(i,0)+1
                print(bin)

    print(f'#{t} {max(bin.values())}')
