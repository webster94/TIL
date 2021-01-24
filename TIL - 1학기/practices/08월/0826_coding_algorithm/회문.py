def examine(sen):
    for i in range(len(sen)//2):
        if sen[i] != sen[-i-1]:
            return False
        else : return True
# 검색기 만듬
for t in range(1,int(input())+1):
    N,M =map(int,input().split())
# 이제 입력을 받자.
    result2 = False
    sent = []
    for i in range(N):
        sent.append(list(input()))
    # print(sent)  오키 입력받았음
    # 행과 열을 검사해야함
    # 행
    for i in range(N):
        for j in range(N-M+1):
            sample = sent[i][j:j+M]
            if examine(sample):
                result = ''.join(sample)
                result1 = True
                break
    # 열
    sub = ''
    sero_list = []
    for i in range(N):
        for j in sent:
            sub += j[i]
        sero_list.append(sub)
        sub = ''
    # print(sero_list) 세로 열 나열에 성공!
    # 이제 다시 쪼개자
    for i in range(len(sero_list)):
        for j in range(len(sero_list)-M+1):
            sample2 = sero_list[i][j:j+M]
            if examine(sample2):
                result = ''.join(sample2)
                result1 = True
                break
    if result1 ==True:
        print('#{} {}'.format(t,result))




