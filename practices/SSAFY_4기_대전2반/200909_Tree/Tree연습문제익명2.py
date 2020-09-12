def pre(num):
    a1.append(num)
    if len(b[num])==2:
        pre(b[num][0])
        pre(b[num][1])
    elif len(b[num])==1:
        pre(b[num][0])
def inorder(num):
    if len(b[num])==2:
        inorder(b[num][0])
        a2.append(num)
        inorder(b[num][1])
    elif len(b[num])==1:
        inorder(b[num][0])
        a2.append(num)
    else:a2.append(num)
def post(num):
    if len(b[num])==2:
        post(b[num][0])
        post(b[num][1])
    elif len(b[num])==1:
        post(b[num][0])
    a3.append(num)

n=int(input())
l=[*map(int,input().split())]
b=[[]for _ in range(n+1)]
a1=[];a2=[];a3=[]
for i in range(len(l)//2):b[l[2*i]].append(l[2*i+1])
tmp=sum(b,[])
for i in set(l):
    if i not in tmp:m=i;break
pre(m)
print(a1)
inorder(m)
print(a2)
post(m)
print(a3)