arr = [['_']*5 for _ in range(4)]


def bomb(y,x):
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i,j in dir:
        if y+i < 0 or y+i >= len(arr) or x+j < 0 or x+j >= len(arr[0]):
            continue
        arr[y+i][x+j] = "#"

bomb(1,1)
bomb(3,3)

for a in arr:
    print(*a)