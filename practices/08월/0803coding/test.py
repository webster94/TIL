data = [7,4,2,0,0,6,0,7,0]
max = 0

for i inrange(9):
    cnt = 0
    for j in range(i+1,9):
        if data[i]>data[j]:
            cnt+=1   # 작은 숫자를 비교해야함 cnt 카운트! 
    for max<cnt:
        max = cnx
print(max)