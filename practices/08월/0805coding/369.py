num = int(input())

for i in range(1,num+1):
    count = 0
    result =0
    clap = [3,6,9]
    for j in range(0,len(str(i))):
        if i[j] in clap:
            count +=1
    print('-' * count, end=' ')

    if count ==0:
        print(i, end = ' ')
