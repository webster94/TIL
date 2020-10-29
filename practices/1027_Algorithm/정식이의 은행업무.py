import sys
sys.stdin = open('정식이의 은행업무.txt','r')
T= int(input())
for t in range(1,T+1):
    btest = list(input())
    ttest = list(input())
    tmp = btest[::]
    dnumber = ''
    result = []
    for i in range(len(btest)):
        # btest = 1010
        for j in range(2):
            if  btest[int(i)] == str(j) :
                continue
            else:
                btest[i] = j  # btest = 0010
                for k in range(len(btest)):
                    dnumber += str(btest[k])
                dnumber = ''.join(dnumber)
                print(dnumber)
                dnumber_t = int(dnumber,2)
                result.append(dnumber_t)
                btest[i] = tmp[i]
                dnumber = ''
    tmp2 = ttest[::]
    tnumber = ''
    result2 = []
    for i in range(len(ttest)):
        # btest = 1010
        for j in range(3):
            if  ttest[i] == str(j) :
                continue
            else:
                ttest[i] = str(j)  # ttest = 212 > 012
                for k in range(len(ttest)):
                    tnumber += str(ttest[k])
                tnumber = ''.join(tnumber) # 3진수로 변경
                print(tnumber)
                tnumber_t = int(tnumber,3) # 3진수에서 10진수로 변경
                result2.append(tnumber_t) # result2 에 추가
                ttest[i] = tmp2[i]
                tnumber = ''
    for i in range(len(result)):
        for j in range(len(result2)):
            # print(result[i], result2[j])
            if result[i] == result2[j]:
                print("#{} {}".format(t,result[i]))

