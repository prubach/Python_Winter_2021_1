l2d = [[5, 5, 7],
       [9, 6, 4],
       [9, 14, 4],
       [1, 4, 5]]
print(l2d[1][2])

#TODO
# 1. sum the rows of l2d [17, 19, 27, 10]
# 2. sum the columns of l2d: [24, 29, 20]
# 3. sum all elements of l2d
#for i in range(len(l2d))

# 1. - simpler solution
sumRow = [sum(i) for i in l2d]
print(sumRow)

# 1. - a manual solution
rows = len(l2d)
cols = len(l2d[0])
sum_rows = []
for i in range(rows):
    sumRow = 0
    for j in range(cols):
        sumRow = sumRow + l2d[i][j]
    sum_rows.append(sumRow)
    print("Sum of " + str(i + 1) + " row: " + str(sumRow))

print(sum_rows)

# 2.
colsum = []
for i in range(len(l2d[0])):
    sum_cols = 0
    for j in range(len(l2d)):
          sum_cols= sum_cols + l2d[j][i]
    print('Sum of column {}'.format(i+1), (sum_cols))
    colsum.append(sum_cols)
print(colsum)

# 3.

sum_all = 0
for el in colsum:
    sum_all += el
print(sum_all)

print(type(colsum))
print(sum(sum_rows))
print(sum(colsum))


import numpy as np

s_rows = np.sum(l2d, axis=1)
print(s_rows)
s_cols = np.sum(l2d, axis=0)
print(s_cols)
