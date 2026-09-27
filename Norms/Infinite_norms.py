A = [
    [2,4,6],
    [7,8,9],
    [2,3,5]
]

row = len(A)
col = len(A[0])

max_row_sum = 0

for i in range(row):
    row_sum = 0
    for j in range(col):
        row_sum += abs(A[i][j])
    if row_sum>max_row_sum:
        max_row_sum = row_sum
print("Infinity norms: ",max_row_sum)
