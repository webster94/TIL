def finder(a,b):
    P= len(a)
    Q = len(b)
    i,j = 0,0
    while i<P and j<Q:
        if a[i] != b[j]:
            i = i - j
            j = -1
        i = i+1
        j = j+1
    if j == Q:
        return i - Q
    else:
        return -1

a= 'minhousealotofkingsleytimewhenlogginghompages'
b= 'kingsley'
print(finder(a,b))