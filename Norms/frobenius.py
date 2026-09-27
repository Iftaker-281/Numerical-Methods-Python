import math
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

row = len(a)
col = len(a[0])

sum_square = 0

for i in range(row):
    for j in range(col):
        sum_square += a[i][j]**2
frobenius = math.sqrt(sum_square)
print("Frobenius: ",frobenius)
