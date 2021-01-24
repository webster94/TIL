

def collage(width):
    # N = 1일 때 가짓수 1개
    if width == N:
        return 1
    # N = 2일 때 가짓수 3개
    if width > N:
        return 0
    # N일 때 가짓수는 직전 단계 가짓수 + 직전의 전 단계 *2(20만큼 늘어나는데 10*2로 넣을 수도 있음)
    return collage(width-1) + collage(width-2)*2

# 정해진 범위 내에서 전부 10 크기의 종이로 먼저 넣고(stack)
# 범위 내에서 10 크기로 전부 채워지면
# 바깥쪽(Last Input)부터 2개씩 묶어서(pop) 20 크기 종이로 치환
# 이 때 10 크기는 가로로 2개 붙이는 것과 세로로 2개 붙이는 것 구분해야 하므로 경우의 수*2
# 20 크기 종이의 수를 세는 변수(cnt_L)를 만듦(stack)
# 총 가짓수 = cnt_L + 1(처음에 10으로 다 넣었던 경우 1개)


T = int(input())

for tc in range(1, T+1):

    print("#{} {}" .format(tc, collage(N)))