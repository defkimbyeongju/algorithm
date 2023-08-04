arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
area = (arr[0][2] - arr[0][0]) * (arr[0][3] - arr[0][1])
comma = []
for i in range(4):
    y, x = arr[i][0], arr[i][2]
    z, w = arr[i][1], arr[i][3]
    for j in range(y,x+1):
        for k in range(z, w+1):
            comma.append((j, k))
comma = list(set(comma))
print(len(comma))