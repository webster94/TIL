arr =[1,2,3,4]
N = 4
R = 2

sel = [0] * R #조합자리만들어줌

def combination(idx,sidx):
    if sidx == R:
        print(sel)
        return
    for i in range(idx,N):
        sel[sidx] = arr[i]
        combination(i+1,sidx +1)
combination(0,0)