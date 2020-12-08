arr = input()
arr =arr.upper()
# 람다를 사용해서
# if 에 0,1 번째의 value값이 같으면 ?을 출력
bin = {}
for i in arr:
    bin[i] = bin.get(i,0) +1
tbin = bin.items()
print(tbin)
sbin = sorted(tbin,key = lambda x:x[1], reverse=True)
if len(sbin) > 1 and sbin[0][1] == sbin[1][1]:
    print('?')
else:
    print(sbin[0][0])