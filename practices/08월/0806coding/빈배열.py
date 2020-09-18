# matrix = [[[0] for _ in range(5) ] for __ in range(5)]
# print(matrix, end = '')
matrix = [[0]*10 for _ in range(10)]

for i in range(10):
    for j in range(10FF):
        matrix[i][j] = 3
        matrix[j][i] = 6

print(matrix)