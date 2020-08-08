# 테스트 케이스
# N = 학생수 , 학점알고싶은 학생의 번호 K
# 테스트 케이스 두번째 줄부터 시험 및 과제 점수가 주어짐

# 입력 받을 때 총점계산
#k 번째 행가서 출력
T = int(input())
for t in range(1,T+1):
    N,K = list(map(int,input().split()))
    result = []
    for stu in range(N):
        total = 0
        M,F,H = list(map(int,input().split()))
        total = (M *0.35 + F * 0.45 + H*  0.25)
        result.append(total)
    # k번째 학생의 시험 점수
    # 이를 위해선 소트해서 몇번째인지 알고 성적부여
    # 소트를 해서 그 위치값을 알고 반환하자
    score = result[K-1]
    result.sort()
    place=result.index(score)
    uni = ['D0', 'C-' , 'C0' ,'C+','B-','B0','B+','A-','A0','A+']  # 비율을 생각못했구만
    li[:]
    print(f'#{t} {uni[place]}')
