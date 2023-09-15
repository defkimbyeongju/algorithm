def bfs(i, j):
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    for y,x in dir:
        ny, nx =

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                bfs(i,j)