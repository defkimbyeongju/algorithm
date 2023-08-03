# map_list = [[3, 3, 5, 3, 1],
#             [2, 2, 4, 2, 6],
#             [4, 9, 2, 3, 4],
#             [1, 1, 1, 1, 1],
#             [3, 3, 5, 9, 2]]
#
# def sum(y, x):
#     total = map_list[y-1][x-1] + map_list[y+1][x-1] + map_list[y+1][x+1] + map_list[y-1][x+1]
#     return total
#
# max_v = 0
# max_row = 0
# max_col = 0
# for i in range(1, len(map_list)-1):
#     for j in range(1, len(map_list[0])-1):
#         if max_v < sum(i,j):
#             max_v = sum(i,j)
#             max_row = i
#             max_col = j
#
# print(max_row, max_col)


# 강사님 방식

arr = [[3, 3, 5, 3, 1],
            [2, 2, 4, 2, 6], 
            [4, 9, 2, 3, 4], 
            [1, 1, 1, 1, 1], 
            [3, 3, 5, 9, 2]]
max_result = 0
max_y = 0
max_x = 0
def sum(y, x):
    direct = [(1,1), (1,-1), (-1,1), (-1,-1)]
    result = 0
    for i,j in direct:
        dir_y = y+i
        dir_x = x+j
        if 0<=dir_y<len(arr) and 0<=dir_x<len(arr[0]):
            result += arr[dir_y][dir_x]
    return result

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if sum(i,j) > max_result:
            max_result = sum(i,j)
            max_y, max_x = i, j

print(max_y, max_x)
