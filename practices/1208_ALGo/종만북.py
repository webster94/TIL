def powerset(index):
    if index == N :
        for i in sel:
            print(i , end= '')
        print()
        return
    sel[index] = 1
    powerset(index+1)
    sel[index] = 0
    powerset(index+1)


N = int(input())
sel = [0] * N
powerset(0)