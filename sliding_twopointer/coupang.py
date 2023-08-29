def bfs(i, j):
    dir = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    for y,x in dir:
        ny, nx = i+y, j+x
        if 0<=ny<N and 0<=nx<N:




N = int(input())
arr = [list(input().split()) for _ in range(N)]
tired = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'P':
