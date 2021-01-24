arr = list(input())
bin = {}
cnt = 0

for i in range(0,len(arr),5):
    bin[i] = bin.get(i,0) + 1
maxbin = 0
for i in bin:
    if bin[i] > maxbin :
        maxbin = bin[i]
tbin=bin.items()
sbin = sorted(tbin,key=lambda x:x[1],reverse=True)
print(" {}".format(sbin[0][0]))