matrix = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]
            max_row, max_col = i + 1, j + 1

print(max_num)
print(max_row, max_col)
