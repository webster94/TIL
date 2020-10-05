N = 10

arr = [1,2,3,4,5,6,7,8,9,10]

sel = [0] * N  # 1을 저장해주기위한 공간, 기록을 위한 공간

def powerset(idx):
    #도착을 했을때
    total = 0
    result = []
    if idx == N:
        for i in range(N):
            if sel[i]:  # 1인 경우 뽑아야지
                total += arr[i]
                result.append(arr[i])
        if total == 10:
            print(result)
        return
    #해당자리를 뽑고 가고
    sel[idx] = 1
    powerset(idx+1)
    #해당자리를 안뽑고 가고
    sel[idx] = 0
    powerset(idx+1)


powerset(0)