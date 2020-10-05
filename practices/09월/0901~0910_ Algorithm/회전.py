# 회전
# 원형큐를 사용한다
# 입력받은리스트의 첫부분을 팝하고 리스트 뒤에 어팬드 가져다 붙인다.
# 인덱스를 초과할 때 길이보다 길어질때 (d+1) % 3 기법을 사용해서 다시 돌린다. # 조금 이상
# count 가 m번이 되었을때 printbreak를 하고 배열의 첫부분을 출력한다
import sys; sys.stdin = open("회전.txt","r")
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    q = list(map(int,input().split()))
    count = 0
    while M>0:
        t = q.pop(0)
        q.append(t)
        M -= 1
    print('#{} {}'.format(tc,q.pop(0)))