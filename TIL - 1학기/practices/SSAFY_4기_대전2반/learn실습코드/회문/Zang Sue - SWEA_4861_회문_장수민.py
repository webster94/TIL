import sys
sys.stdin = open("input_4861.txt" ,"r")

def check(texts):
    result = []
    for text in texts:
        for i in range(N-M+1):
            if text[i:i+M-1] == text[i+M-1:i:-1]:
                result = ''.join(text[i:i+M])
    return result

def rotate(texts):
    words = []
    for i in range(N):
        word = []
        words.append(word)
        for j in range(N):
            word.append(texts[j][i])
    return words

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    texts = [list(input()) for _ in range(N)]
    row = check(texts)
    if row:
        result = row
    else:
        col = rotate(texts)
        result = check(col)
    print('#{} {}'.format(tc, result))