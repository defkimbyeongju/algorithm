n, m = map(int, input().split())
k = int(input())
arr = [[] for _ in range(k+1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[b].append((i,j))
sx, sy, dx, dy = map(int, input().split())
print(arr)
