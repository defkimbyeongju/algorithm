# N = 2
# M = 4
# arr = [[0, 1,  2, 3],[4, 5, 6, 7]]
#
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1-2*j)*(i%2)])


N = 2
M = 4
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total

print(max_v)