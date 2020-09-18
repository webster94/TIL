def Hyeunwoo(sentence,pattern):
    i,j = 0,0
    while (i < len(sentence) and j < len(pattern)):
        if sentence[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1






sentence = '나는 오늘 보충이 끝난 8시에, 현우와 함께 공부를 하기위해서 은묵이형네로 출발했다.'
search = '현우'
print(Hyeunwoo(sentence,search))