def brute(t,p):
    i,j = 0,0
    while j < len(p) and i < len(t):  # j는 검색기, i 검색기
        if t[i] != p[j]: # 다른 요소를 찾았다.
            i = i - j  #i = 0
            j = -1 # j= -1로 정의
        i += 1  # i는 앞으로 한칸이동
        j += 1 #J = 0
    if j ==len(p):  # 같은 패턴 찾았다 # j와 패턴의 길이가 같다.
        return i - len(p)    # 패턴의 시작 장소를 리턴
    else:   # 못찾으면 -1
        return -1

text = "TTTTTTAACCA"
pattern = "TTA"

print(brute(text, pattern))
print(text.find(pattern))