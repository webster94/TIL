# 미완성입니다.
# 1= 10짜리 세로블럭, 2 = 10짜리 가로블럭, 3 = 20짜리
# 종이붙이기한 모양을 리스트로 생각(1,1,1 이렇게)
# 방문체크(already)에 모양 리스트 넣기
# 방문체크에 없다면, 리스트에 append
# 정답 = 리스트 길이

def check(li):
    li_copy = li[:]
    for i in range(N):
        if li[i:i+2] = [1, 1]: # 1을 3으로 변경
            li_copy.insert(i,3) # i,i+1 위치의 1을 3,0으로 변경
            li_copy.insert(i+1,0)
            already.li # 변경값을 방문체크에 추가
        elif li[i] == 3: # 3을 2로 쪼개기
            li[i:i+2] = [3, 0]:
            li.



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    rec = [1] * N #1은 10짜리 세로블럭
    already = [rec] # 이미 만들어진 구성
    ans = check(rec)

