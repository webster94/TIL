pattern = {'S':0, 'D':1, 'H':2, 'C':3}

T = int(input())

for tc in range(1, T+1):
    line = input()

    card = [[0] * 14 for _ in range(4)]

    #에러인지 아닌지를 위한 bool 변수
    is_error = False

    for i in range(0, len(line), 3):
        #패턴
        card_p = pattern[line[i]]
        #번호
        card_n = int(line[i+1:i+3])

        #이미 가지고 있는 카드라면 종료
        if card[card_p][card_n] == 1:
            is_error = True
            break
        #그게아니라면 카드 표시
        card[card_p][card_n] = 1
        #0인덱스는 카드 카운팅을 위해 사용
        card[card_p][0] += 1

    print("#{}".format(tc), end=" ")
    if is_error:
        print("ERROR")
    else:
        for i in range(4):
            print("{}".format(13-card[i][0]), end=" ")
        print()