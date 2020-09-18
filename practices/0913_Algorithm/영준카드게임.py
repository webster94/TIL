import sys
sys.stdin = open("영준카드게임.txt","r")
# A =

T = int(input())
for t in range(1,T+1):
    resultS = 13
    resultD = 13
    resultH = 13
    resultC = 13
    flag = False
    cards = input()
    check = []
    for i in range(0,len(cards),3):
        char = cards[i]
        number = str(cards[i+1]+cards[i+2])
        if [char + number] in check:
            flag = True
            break
        check.append([char + number])
    print("#{}".format(t),end = " ")
    if flag :
        print("ERROR")
        continue
    for i in check:
        for j in i:
            if "S" in j:
                resultS -= 1
            if "D" in j:
                resultD -= 1
            if "H" in j:
                resultH -= 1
            if "C" in j:
                resultC -= 1

    print("{} {} {} {}".format(resultS,resultD,resultH,resultC))

