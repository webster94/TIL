row_start = 0
row_end = 4
col_start = 0
col_end = 4

while row_start <= row_end and col_start <= col_start:
    # 왼쪽 => 오른쪽
    for i in range(col_start, col_end +1):
        arr[row_start][i]= cnt
        cnt +=1
    row_start +=1
    # 위쪽 => 아래
    for i in range(row_start,row_end + 1):
        arr[i][col_end] = cnt
        cnt +=1
    col_end -=1
    # 오른쪽 => 왼쪽
    for i in range(col_end,col_start-1,-1):
        arr[row_end][i]= cnt
        cnt +=1
    # 아래 => 위
    for i in range(row_end,row_start -1,-1):
        arr[i][col_end]
    col_start +=1
print(arr)