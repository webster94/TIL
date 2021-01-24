
X = int(input())
num = 1
while X > num :
    X -= num
    num += 1
if num %2 == 0:
    a = X
    b = num - X + 1
else:
    a = num - X + 1
    b = X

print(a,'/',b,sep='' )
