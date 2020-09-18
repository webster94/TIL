def check():
    for i in range(9):
        # 해당 숫자를 사용했는지 체크
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행검사
            num1 = sudoku[i][j]
            # 열검사
            num2 = sudoku[j][i]
            # 이미 사용한 숫자라면 유효한 스도쿠가 아니라서 0을 리턴
            if row[num1]:
                return 0
            if col[num2]:
                return 0
            # 위에 걸리지 않았다면 사용했음을 표시
            row[num1] = col[num2] = 1

            # 0~8까지 사용이 가능하므로 0, 3, 6 일때 걸리게 됩니다.
            # 3x3검사
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1

    # 위에서 리턴되지 않았다면 유효한 스도쿠입니다.
    return 1


T = int(input())

for tc in range(1, T + 1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if check():
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
