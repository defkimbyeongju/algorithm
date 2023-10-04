from collections import deque
# 조합
def


# 바이러스 퍼지기
def virus(arr):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                queue.append((i,j))
    while queue:
        now_y, now_x = queue.popleft()
        for y,x in dir:
            ny, nx = now_y+y, now_x+x
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
                arr[ny][nx] = 2
                queue.append((ny,nx))
    arr = sum(arr, [])
    return arr.count(0)

N,M = map(int,input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
safe = [] # 0인 구역
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            safe.append((i,j))
