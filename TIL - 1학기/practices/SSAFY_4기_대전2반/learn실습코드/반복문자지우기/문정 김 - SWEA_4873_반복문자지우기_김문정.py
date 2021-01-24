
def erase(texts):
    for i in range(len(texts)-1):
        if texts[i] == texts[i+1]:
            texts.remove(texts[i])
            texts.remove(texts[i]) # 위에서 원소하나를 지워서 idx가 줄어든다. 기존의 i+1번째가 i번째가 된다.
            temp = texts[:]
            return erase(temp)
    return len(texts)

T = int(input())
for tc in range(1, T+1):
    sentences = list(input())
    # print(sentences)
    print('#{} {}'.format(tc, erase(sentences)))
