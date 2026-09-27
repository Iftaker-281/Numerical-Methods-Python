A = [
    [1,2,3],
    [2,4,5],
    [6,7,8]
]
row = len(A)
col = len(A[0])

max_column_sum = 0;

for j in range(col):
    col_sum = 0
    for i in range(row):
        col_sum += abs(A[i][j])
    if col_sum>max_column_sum:
        max_col_sum = col_sum

print("1-Norms: ",max_col_sum)
